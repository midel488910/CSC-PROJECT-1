from django import forms

class createNewList(forms.Form):
    name = forms.CharField(label="Name",max_length=255)
    check = forms.BooleanField(required=False)
     