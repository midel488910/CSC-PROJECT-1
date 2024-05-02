from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return
        HttpResponseRedirect("http://127.0.0.1:8000/")
    
    return render(request, "register/registration.html", {"form": form})

