from django.views.generic import DetailView

from app.models import Cocktail


class CocktailDetailView(DetailView):
    template_name = 'cocktail_detail.html'
    model = Cocktail
