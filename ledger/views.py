from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage


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

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})

        

class RecipeImageCreateView(LoginRequiredMixin, CreateView):

    model = RecipeImage
    fields = ['image', 'description']
    template_name = "ledger/add_image.html"

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.kwargs['pk']})