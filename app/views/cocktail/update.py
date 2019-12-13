from django.urls import reverse
from django.views.generic import UpdateView

from app.forms.cocktail import CocktailForm
from app.models import Cocktail


class CocktailUpdateView(UpdateView):
    template_name = 'cocktail_update.html'
    model = Cocktail
    form_class = CocktailForm

    def get_success_url(self):
        return reverse('app_cocktail_list')