from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movies_count'.split()
        

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)

    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()
        


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)

    class Meta:
        model = Movie
        fields = 'id title description duration director reviews'.split()
        depth = 1


class MovieReviewSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)

    class Meta:
        model = Movie
        fields = 'id title description duration director average_review reviews'.split()
        depth = 1
        

        