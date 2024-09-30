from django.db import models
from django.conf import settings


# patrón de normalización de modelos

# Separar Ingredientes de Recetas: se creó una nueva clase Ingredient que representará los ingredientes de forma independiente.

# Establecer una Relación Muchos-a-Muchos: Dado que una receta puede tener muchos ingredientes y un ingrediente puede estar en muchas recetas,
# utilizaremos una relación muchos-a-muchos

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)  # Relación muchos-a-muchos con Ingredient
    generation_date = models.DateField(auto_now_add=True)
    image = models.URLField(blank=True, null=True)
    cuisine = models.TextField()
    number_of_portions = models.TextField()
    favourite_state = models.BooleanField(default=False)

    