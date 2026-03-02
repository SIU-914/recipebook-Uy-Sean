from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('accounts/login/',
         auth_views.LoginView.as_view(
             template_name='registration/login.html',
             redirect_authenticated_user=True
         ),
         name='login'),

    path('accounts/logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),

    path('accounts/', include('django.contrib.auth.urls')),

]

