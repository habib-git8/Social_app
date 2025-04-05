"""
This module contains the views for the feed app, handling user authentication,
post creation, and user profile management.
"""
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, CustomUserCreationForm, PostForm
from .models import Post
from django.contrib import messages
def home(request):
    """
    Render the home page.
    """
    return render(request, 'feed/home.html')
def profile(request):
    """
    Render the user profile page.
    """
    return render(request, 'feed/profile.html')
def feed(request):
    """
    Display the feed with all posts, ordered by creation date (latest first).
    """
    posts = Post.objects.all().order_by('-created_at')  # Fetch posts, latest first
    return render(request, 'feed/feed.html', {'posts': posts})
def post(request):
    """
    Render the page for creating a new post.
    """
    return render(request, 'feed/post.html')
def user_login(request):
    """
    Handle user login. Authenticate the user and redirect to the feed.
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("feed")  # Redirect to feed after login
        else:
            return render(request, "feed/login.html", {"error": "Invalid credentials"})
    return render(request, "feed/login.html")
@login_required
def user_logout(request):
    """
    Handle user logout. Log out the user and redirect to login page.
    """
    logout(request)
    return redirect("login")
def signup(request):
    """
    Handle user signup. If the form is valid, save the user and redirect to login page.
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login after signup
    else:
        form = CustomUserCreationForm()
    return render(request, "feed/signup.html", {"form": form})
@login_required
def create_post(request):
    """
    Create a new post. If the form is valid, save the post and redirect to the feed.
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Save but don't commit to DB yet
            post.user = request.user  # Set the user before saving
            post.save()
            return redirect('feed')  # Redirect to feed after posting
    else:
        form = PostForm()
    
    return render(request, 'feed/post.html', {'form': form})
@login_required
def update_post(request, post_id):
    """
    Update an existing post. Only the post owner can update it.
    """
    post_instance = get_object_or_404(Post, id=post_id, user=request.user)  # Ensure only owner can edit
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post_instance)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm(instance=post_instance)
    return render(request, 'feed/update_post.html', {'form': form})
@login_required
def delete_post(request, post_id):
    """
    Delete an existing post. Only the post owner can delete it.
    """
    post_instance = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == "POST":
        post_instance.delete()
        return redirect('feed')
    
    return render(request, 'feed/delete_post.html', {'post': post_instance})
