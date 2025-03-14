from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content', 'rows': 4}),  
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

        error_messages = {
            'title': {'required': 'Post title is required'},
            'content': {'required': 'Please provide some content'},
            'image': {'required': 'Please upload an image'},
        }

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Ensure email is required

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match. Please enter the same password.")

        return cleaned_data
