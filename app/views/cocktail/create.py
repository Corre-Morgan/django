from django.urls import reverse
from django.views.generic import CreateView

from app.forms.cocktail import CocktailForm
from app.models import Cocktail


class CocktailCreateView(CreateView):
    template_name = 'cocktail_create.html'
    model = Cocktail
    form_class = CocktailForm

    def get_success_url(self):
        return reverse('app_cocktail_list')