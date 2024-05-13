from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from .forms import RegisterForm, CaseForm
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import CaseFile
from django.views import generic
from django.db.models import Q


# Create your views here.

def Base(request):
    return render(request,"main/base.html")

def search_view(request):
    if request.method == "POST":
        if "pdf-id" in request.POST: # from templates of html a button named pdf-id is passed
            pdf_id = request.POST.get('pdf-id')
            pdf = CaseFile.objects.get(id=pdf_id)
            if pdf and (request.user.has_perm("main.delete_post")):
                pdf.delete()
        elif "searched" in request.POST: # from templates of html an input named search is passed
            searched = request.POST['searched']
            print(searched)
            pdf_files = CaseFile.objects.filter(
                Q(title__icontains=searched)|
                Q(respondents__icontains=searched)|
                Q(docket_number__icontains=searched)|
                Q(date_of_decision__icontains=searched)|
                Q(remarks__icontains=searched))
            print(pdf_files)
            return render(request, 'main/search_results.html',{'searched': searched,'pdf_files':pdf_files})
        else:
            return render(request, 'main/search_results.html',{})
    else:
        return render(request, 'main/search_results.html',{})



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
    logout(request)
    return redirect('login')

@login_required(login_url="/login")   
@permission_required('main.add_post',login_url="/login",raise_exception=True)
def upload_pdf(request):
    if request.method == "POST":
        form = CaseForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('Home')
    else:
        form = CaseForm()
    return render(request,'main/upload_pdf.html',{'form':form})
#PDFView(generic.TemplateView):
@login_required(login_url="/login")   
def PDFView(request):
    pdf_files = CaseFile.objects.all()
    if request.method == "POST":
        pdf_id = request.POST.get('pdf-id')
        pdf = CaseFile.objects.get(id=pdf_id)
        if pdf and (pdf.author == request.user or request.user.has_perm("main.delete_post")):
            pdf.delete()
    
    return render(request, "main/home.html",{"pdf_files":pdf_files})
    

 

