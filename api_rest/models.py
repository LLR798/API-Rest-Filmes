from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

import datetime



class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(
        max_length=150, default='')
    movie_year = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(datetime.date.today().year),
        ],
        default=0
    )
    movie_description = models.TextField(max_length=900, default='')
    movie_time = models.CharField(max_length=11, default='0 minutos')
    movie_category = models.CharField(max_length=50, default='')
    movie_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    def __str__(self):
        return f"Movie name: {self.movie_name}\nRating: {self.movie_rating}"
