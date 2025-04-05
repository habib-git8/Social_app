from django.urls import path
from django.http import HttpResponse
from . import views
urlpatterns = [
    path('', views.home),
    path('profile/', views.profile),
    path('feed/', views.feed, name='feed'),
    path('post/', views.create_post, name='create_post'),
     path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
        path('update/<int:post_id>/', views.update_post, name='update_post'),  # Edit post
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'), 
]