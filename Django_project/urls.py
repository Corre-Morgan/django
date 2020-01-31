"""Django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from app.views.cocktail.create import CocktailCreateView
from app.views.cocktail.delete import CocktailDeleteView
from app.views.cocktail.detail import CocktailDetailView
from app.views.cocktail.list import CocktailListView
from app.views.cocktail.search import CocktailSearchDetailView
from app.views.cocktail.update import CocktailUpdateView
from app.views.cocktail.search_by_ingredient import CocktailSearchByIngredientView
from app.views.index import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('cocktails/detail/<int:pk>', CocktailDetailView.as_view(), name='app_coktail_detail'),
    path('cocktails/detail/search/<str:slug>', CocktailSearchDetailView.as_view(), name='app_coktail_search_detail'),
    path('cocktails/create', CocktailCreateView.as_view(), name='app_cocktail_create'),
    path('cocktails/delete/<int:pk>', CocktailDeleteView.as_view(), name='app_cocktail_delete'),
    path('cocktails/update/<int:pk>', CocktailUpdateView.as_view(), name='app_cocktail_update'),
    path('cocktails/list', CocktailListView.as_view(), name='app_cocktail_list'),
    path('cocktails/search-by-ingredient/<str:slug>', CocktailSearchByIngredientView.as_view(), name='app_cocktail_list'),
]
