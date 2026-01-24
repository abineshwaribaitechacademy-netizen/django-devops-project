from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),

    # category URLs
    path('mobiles/', views.mobiles, name='mobiles'),
    path('shoes/', views.shoes, name='shoes'),
    path('cakes/', views.cakes, name='cakes'),
    path('drinks/', views.drinks, name='drinks'),

    # product detail page
    path('product/<int:pk>/', views.product, name='product'),
]
