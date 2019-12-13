from django.urls import reverse_lazy
from django.views.generic import DeleteView

from app.models import Cocktail


class CocktailDeleteView(DeleteView):
    template_name = 'cocktail_delete.html'
    model = Cocktail
    success_url = reverse_lazy('app_cocktail_list')
