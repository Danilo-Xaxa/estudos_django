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
    form = CreateNewList()
    return render(request, "principal/create.html", {"form": form})