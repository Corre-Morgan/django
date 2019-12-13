from django.views import generic

from app.models import Cocktail, Ingredient, CocktailIngredientUnit


class CocktailSearchByIngredientView(generic.ListView):
    template_name = 'cocktail_list.html'

    def get_queryset(self):
        search = self.kwargs['slug']
        # result = []
        # for ingredient in Ingredient.objects.filter(description__icontains=search):
        #    for ciu in CocktailIngredientUnit.objects.filter(ingredient=ingredient):
        #        result.append(ciu.cocktail) c'est la meme chose que le return
        return Cocktail.objects.filter(ingredients__ingredient__description__icontains=search)
