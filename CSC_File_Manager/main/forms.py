from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Dog



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]


class PostForm(forms.ModelForm):
    file = forms.FileField()
    class Meta:
        model = Post
        fields = ['title','description']

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name','image']