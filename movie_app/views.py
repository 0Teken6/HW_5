from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from . import serializers as my_serializers
from rest_framework import status


@api_view(["GET"])
def director_list_api_view(request):
    directors = Director.objects.all()

    data = my_serializers.DirectorSerializer(directors, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(["GET"])
def director_detail_api_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Director not found'})
    except Director.MultipleObjectsReturned:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = my_serializers.DirectorSerializer(directors).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(["GET"])
def movie_list_api_view(request):
    movies = Movie.objects.all()

    data = my_serializers.MovieSerializer(movies, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(["GET"])
def movie_detail_api_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Movie not found'})
    except Movie.MultipleObjectsReturned:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = my_serializers.MovieSerializer(movies).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(["GET"])
def review_list_api_view(request):
    reviews = Review.objects.all()

    data = my_serializers.ReviewSerializer(reviews, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)


@api_view(["GET"])
def review_detail_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Review not found'})
    except Review.MultipleObjectsReturned:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    data = my_serializers.ReviewSerializer(reviews).data

    return Response(data=data, status=status.HTTP_200_OK)