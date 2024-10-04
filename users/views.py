from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, UserAuthSerializer, CodeConfirmationValidator
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import ConfirmCode
from rest_framework.permissions import IsAuthenticated


@api_view(["POST"])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = User.objects.create_user(username=username, password=password, is_active=False)
    confirmation_code = ConfirmCode.objects.create(user=user)

    return Response(status=status.HTTP_201_CREATED, 
                    data={'user_id': user.id,
                          'confirmation_code': confirmation_code.code})


@api_view(['POST'])
def confirm_user_api_view(request):
    serializer = CodeConfirmationValidator(data=request.data)
    serializer.is_valid()

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']
    code = serializer.validated_data['code']

    try:
        user = User.objects.get(username=username)
        if not user.check_password(password):
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    code_obj = ConfirmCode.objects.get(user=user)

    if code_obj.code == code:
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_202_ACCEPTED,
                        data={"success": 'User is now active'})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={'error': 'Wrong code!'})

@api_view(["POST"])
def authorization_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(**serializer.validated_data)

    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key},
                        status=status.HTTP_200_OK if not created 
                        else status.HTTP_201_CREATED)
    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data={'error': 'User credentials are wrong'})