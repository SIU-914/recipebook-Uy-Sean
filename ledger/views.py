from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = "ledger/recipe_list.html"
    context_object_name = "recipes"


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipe_detail.html", {"recipe": recipe})

class RecipeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"