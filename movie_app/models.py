from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def movies_count(self):
        return len(self.movies.all())
    

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(help_text='In minutes')
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='movies')

    def __str__(self):
        return self.title
    
    def average_review(self):
        reviews = self.reviews.all()
        if not reviews:
            return 0
        total_stars = sum(review.stars for review in reviews)
        return total_stars / len(reviews)


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'Review for {self.movie.title}'