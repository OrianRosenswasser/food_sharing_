from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('food_feed/', views.food_feed, name='food_feed'),
    path('post_food/', views.post_food, name='post_food'),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('request_food/<int:food_post_id>/', views.request_food, name='request_food'),
]
