from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import redirect, render
from .models import ToDoList, Item
from .forms import CreateNewList
from django.contrib.auth.models import AnonymousUser


def index(request):
    return render(request, "principal/index.html", {})


def todo_list(request, id):
    try:
        ls = ToDoList.objects.get(id=id)
    except ToDoList.DoesNotExist:
        ls = None

    if isinstance(request.user, AnonymousUser):
        return HttpResponseRedirect("/") 

    if ls in request.user.todolist.all():
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
    else:
        return HttpResponseRedirect("/")


def create(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)
        return HttpResponseRedirect(f"/{t.id}")
    else:
        form = CreateNewList()
        return render(request, "principal/create.html", {"form": form, 'x': request.POST})


def view(request):
    return render(request, "principal/view.html", {"user": request.user})

def home(request):
    return redirect("/")