from django.views import generic
from .models import Recipe
class RecipeListView(generic.ListView):
    model = Recipe
    template_name = "ledger/recipe_list.html"
    context_object_name = "recipes"


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"