from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.first),
    path('second/', views.second),
    path('filterbrand/', views.filterbrand),
]