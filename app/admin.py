from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from app.models import Cocktail, Unit, Ingredient, CocktailIngredientUnit, Tag, CocktailTag


class CocktailTagInlineAdmin(admin.StackedInline):
    model = CocktailTag
    extra = 0


class CocktailIngredientUnitInlineAdmin(admin.StackedInline):
    model = CocktailIngredientUnit
    extra = 0


class CocktailAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'recipe')
    list_display = ('title', 'custom_description')
    list_display_links = list_display
    inlines = (CocktailIngredientUnitInlineAdmin, CocktailTagInlineAdmin)

    def custom_description(self, obj):
        return format_html('<b>DESCRIPTION </b>: {}'.format(obj.description[:80]))

    custom_description.short_description = 'Summary'


admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(Unit)
admin.site.register(Ingredient)
admin.site.register(CocktailIngredientUnit)
admin.site.register(Tag)
admin.site.register(CocktailTag)
