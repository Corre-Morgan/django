from django.views.generic import ListView

from app.models import Cocktail


class CocktailListView(ListView):
    template_name = 'cocktail_list.html'
    model = Cocktail