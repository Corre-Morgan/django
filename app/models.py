from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Cocktail(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, default='(no title)')
    description = models.TextField(blank=True, null=True, default=None)
    recipe = models.TextField(blank=True, default=True, null=False)
    tags = models.ManyToManyField('Tag', related_name='cocktails', through='CocktailTag')

    def __str__(self):
        return self.title if self.title is not None else '????????'


class CocktailTag(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)


class Unit(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True, default='(no title)')

    def __str__(self):
        return self.description if self.description is not None else '????????'


class Ingredient(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True, default='(no title)')

    def __str__(self):
        return self.description if self.description is not None else '????????'


class CocktailIngredientUnit(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE, default=None, null=True, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, default=None, null=True)
    value = models.FloatField(default=1.0, blank=False)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return '{} {} {}'.format(self.value, self.unit, self.ingredient)


class Tag(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True, default='(no title)')
