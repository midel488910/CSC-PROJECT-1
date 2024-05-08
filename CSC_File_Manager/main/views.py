from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from .forms import RegisterForm, PostForm, CaseForm
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Post, CaseFile
from django.views import generic


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


def upload_pdf(request):
    if request.method == "POST":
        form = CaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = CaseForm()
    return render(request,'main/upload_pdf.html',{'form':form})
#PDFView(generic.TemplateView):
def PDFView(request):
    # model = CaseFile
    # template_name = 'display_pdf.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["pdfFiles"] = CaseFile.objects.all()
    #     return context
    pdf_files = CaseFile.objects.all()
    return render(request, "main/display_pdf.html",{"pdf_files":pdf_files})
    

 

