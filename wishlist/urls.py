from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.wishlist_add, name='wishlist_add'),
    path('', views.wishlist_summary, name='wishlist_summary'),
]
