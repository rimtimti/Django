from django.urls import path
from . import views

urlpatterns = [
    path("eagle/", views.eagle, name="eagle"),
    path("cube/", views.cube, name="cube"),
    path("random_number/", views.random_number, name="random_number"),
    path("show_coins/<int:n>", views.show_coins, name="show_coins"),
]
