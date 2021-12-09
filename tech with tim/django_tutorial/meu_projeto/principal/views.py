from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import ToDoList, Item
from .forms import CreateNewList


def index(request):
    return render(request, "principal/index.html", {})

def todo_list(request, id):
    todo_list = ToDoList.objects.get(id=id)
    items = todo_list.item_set.all()
    variaveis = {"todo_list": todo_list, "items": items}
    return render(request, "principal/todo_list.html", variaveis)

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
