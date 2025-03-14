
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm , CustomUserCreationForm 
from .models import Post
from .forms import PostForm
from django.conf import settings
def home(request):
    return render(request, 'feed/home.html')

def profile(request):
    return render(request, 'feed/profile.html')

def feed(request):
    posts = Post.objects.all().order_by('-created_at')  # Fetch posts, latest first
    return render(request, 'feed/feed.html', {'posts': posts}) 
def post(request):
    return render(request, 'feed/post.html')
def user_login(request):
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

# Logout View
@login_required
def user_logout(request):
    logout(request)
    return redirect("login")

def signup(request):
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
    post = get_object_or_404(Post, id=post_id, user=request.user)  # Ensure only owner can edit
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'feed/update_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == "POST":
        post.delete()
        return redirect('feed')
    
    return render(request, 'feed/delete_post.html', {'post': post})