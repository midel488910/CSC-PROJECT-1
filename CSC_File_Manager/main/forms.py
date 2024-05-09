from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, CaseFile



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','description']


class CaseForm(forms.ModelForm):
    class Meta:
        model = CaseFile
        widgets = {
            'date_of_decision': forms.DateInput(attrs={'type': 'date'})
        }
        fields = ('title','docket_number','filePdf','date_of_decision','respondents','remarks')



