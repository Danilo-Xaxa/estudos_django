from django.shortcuts import render
from .models import ToDoList, Item


def index(request):
    return render(request, "principal/index.html", {})

def todo_list(request, id):
    todo_ls = ToDoList.objects.get(id=id)
    first_item = todo_ls.item_set.get(id=1)
    return render(request, "principal/todo_list.html", {"todo_list_name": todo_ls.name, "first_item_text": first_item.text})
