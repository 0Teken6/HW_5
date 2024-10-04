from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from . import serializers as my_serializers
from rest_framework import status


@api_view(["GET", "POST"])
def director_list_api_view(request):
    if request.method == 'GET':

        directors = Director.objects.all()

        data = my_serializers.DirectorSerializer(directors, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        name = request.data.get('name')
        
        director = Director.objects.create(
            name=name
        )

        return Response(status=status.HTTP_201_CREATED, 
                        data=my_serializers.DirectorSerializer(director).data)


@api_view(["GET", "PUT", "DELETE"])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Director not found'})
    except Director.MultipleObjectsReturned:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        data = my_serializers.DirectorSerializer(director).data

        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        director.name = request.data.get('name')
        director.save()

        return Response(status=status.HTTP_201_CREATED, 
                        data=my_serializers.DirectorSerializer(director).data)
    
    elif request.method == "DELETE":
        director.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        data = my_serializers.MovieSerializer(movies, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        title = request.data.get('title')
        description = request.data.get("description")
        duration = request.data.get("duration")
        director_id = request.data.get("director_id")

        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )

        return Response(status=status.HTTP_201_CREATED, 
                        data=my_serializers.MovieSerializer(movie).data)


@api_view(["GET"])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Movie not found'})
    except Movie.MultipleObjectsReturned:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        data = my_serializers.MovieDetailSerializer(movie).data

        return Response(data=data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()

        return Response(status=status.HTTP_201_CREATED, 
                        data=my_serializers.MovieSerializer(movie).data)
    
    elif request.method == "DELETE":
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        data = my_serializers.ReviewSerializer(reviews, many=True).data

        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        text = request.data.get('text')
        stars = request.data.get("stars")
        movie_id = request.data.get("movie_id")

        review = Review.objects.create(
            text=text,
            stars=stars,
            movie_id=movie_id,
        )

        return Response(status=status.HTTP_201_CREATED, 
                        data=my_serializers.ReviewSerializer(review).data)

@api_view(["GET"])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Review not found'})
    except Review.MultipleObjectsReturned:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        data = my_serializers.ReviewSerializer(review).data

        return Response(data=data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie_id = request.data.get('movie_id')
        review.save()

        return Response(status=status.HTTP_201_CREATED, 
                        data=my_serializers.ReviewSerializer(review).data)
    
    elif request.method == "DELETE":
        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def movies_reviews_api_view(request):
    movies = Movie.objects.all()

    data = my_serializers.MovieReviewSerializer(movies, many=True).data

    return Response(data=data, status=status.HTTP_200_OK)