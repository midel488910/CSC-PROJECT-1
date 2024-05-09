from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, CaseFile



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        #arrangement in the website 
        fields = ["username","first_name", "last_name" ,"email", "password1","password2"]


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','description']


class CaseForm(forms.ModelForm):
    class Meta:
        model = CaseFile
        fields = ('title','docket_number','filePdf','date_of_decision','respondents','remarks')
        widgets = {
            'date_of_decision': forms.DateInput(attrs={'type': 'date'}),
            'filePdf': forms.FileInput(attrs={'accept': '.pdf'})
        }
        



