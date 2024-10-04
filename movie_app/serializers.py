from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


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
        

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=255)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=255)
    description = serializers.CharField(required=False, default='No text')
    duration = serializers.IntegerField(min_value=0)
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except:
            raise ValidationError("Director not found") 
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField()
    movie_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except:
            raise ValidationError("Director not found") 
        return director_id
    
    def validate_start(self, stars):
        if stars not in range(1, 6):
            raise ValidationError("Stars should be from 1 to 5") 
        return stars
