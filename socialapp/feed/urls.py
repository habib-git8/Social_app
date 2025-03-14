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
    # path('contact/', views.create_post),
    # path('feed/', views.feed, name='feed'),  # View all posts
    # path('create/', views.create_post, name='create_post'),  # Create post
    # path('update/<int:post_id>/', views.update_post, name='update_post'),  # Edit post
    # path('delete/<int:post_id>/', views.delete_post, name='delete_post'), 
    # path("signup/", views.signup, name="signup"),
    # path("login/", views.user_login, name="login"),
    # path("logout/", views.user_logout, name="logout"),
    # path("donation/", views.donation, name="donation"), 
    # path('donate/<int:post_id>/', views.donation_page, name='donation_page'),
    # path('paypalpayment/<int:post_id>/', views.paypalpayment, name='paypalpayment'),
    # path('paypal-success/', views.paypal_success, name='paypal_success'),
    # path('paypal-cancel/', views.paypal_cancel, name='paypal_cancel'),
]