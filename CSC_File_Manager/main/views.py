from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post

# Create your views here.

def Base(request):
    return render(request,"main/base.html")

@login_required(login_url="/login")
def Home(request):
    posts = Post.objects.all()
    if request.method == "POST":
        post_id = request.POST.get('post-id')
        post = Post.objects.get(id=post_id)
        if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
            post.delete()

    return render(request,"main/home.html",{'posts':posts})

def SignUp(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('Home')
    else:
        form = RegisterForm()
    return render(request,"registration/sign_up.html", {'form':form})

def logout_view(request):
    messages.add_message(request, messages.INFO, "You have been logged out")
    messages.info(request,"HELLOW WORLD")
    logout(request)
    return redirect('login')


@login_required(login_url="/login")   
@permission_required('main.add_post',login_url="/login",raise_exception=True)
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('Home')
    else:
        form = PostForm()
    return render (request,'main/create_post.html',{'form':form})




 

