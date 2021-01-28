from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    process = models.TextField()
    image = models.ImageField(upload_to='images')
