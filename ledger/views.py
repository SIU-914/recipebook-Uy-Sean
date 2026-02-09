from django.shortcuts import render

def recipe_list(request):
    return render(request, 'ledger/recipes_list.html')

def recipe_1(request):
    return render(request, 'ledger/recipe_1.html')

def recipe_2(request):
    return render(request, 'ledger/recipe_2.html')