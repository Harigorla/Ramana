from django.db import models


class Recipe(models.Model):
    description = models.TextField("Description")
    ingredients = models.TextField("Ingredients")
    preparation = models.TextField("Preparation")
    image = models.ImageField(upload_to='recipes/%Y/%m/%d')
    created = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.description
