from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import render
from .models import ToDoList, Item
from .forms import CreateNewList


def index(request):
    return render(request, "principal/index.html", {})


def todo_list(request, id):
    ls = ToDoList.objects.get(id=id)
 
    if request.method == "POST":
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
    
                item.save()
    
        elif request.POST.get("newItem"):
            txt = request.POST.get("new")
    
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")
    
    return render(request, "principal/todo_list.html", {"todo_list":ls})


def create(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST)
        if form.is_valid():
            todo_list = ToDoList(name=form.cleaned_data["name"])
            todo_list.save()
            return HttpResponseRedirect(f"/{todo_list.id}")
    else:
        form = CreateNewList()
        return render(request, "principal/create.html", {"form": form, 'x': request.POST})
