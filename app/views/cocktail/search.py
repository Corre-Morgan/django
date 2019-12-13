from django.views.generic import ListView

from app.models import Cocktail


class CocktailSearchDetailView(ListView):
    template_name = 'index.html'
    model = Cocktail

    def get_queryset(self):
        title = self.kwargs.get('slug', '')
        return Cocktail.objects.filter(title__contains=title)