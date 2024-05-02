from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import todoList, Item
from .forms import createNewList
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def Base(request):
    return render(request,"base.html")

def Home(request):
    #return HttpResponse("WELCOME")
    names = todoList.objects.all()
    return render(request,"home.html",{"names":names})

def Details(request,id):
    ls = todoList.objects.get(id=id)
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c"+str(ls.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif request.POST.get("newItem"):
            txt = request.POST.get("new")
            if len(txt)>2:
                ls.item_set.create(text=txt,complete=False)
            else:
                print("Invalid")
    return render(request,"details.html",{"ls": ls})

def Create(request):
    request.user
    if request.method == "POST":
        form = createNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            request.user.todoList_set.create(name=n)
            
        return HttpResponseRedirect("/Home/details/%i" %t.id)
    else:
        form = createNewList()

    return render(request, "create.html",{"form":form})

 