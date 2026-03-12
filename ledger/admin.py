from django.contrib import admin
from .models import Ingredient,Recipe, RecipeIngredient,RecipeImage
from .models import Profile


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    inlines = [RecipeImageInline]



    

admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Profile)
admin.site.register(RecipeImage)
