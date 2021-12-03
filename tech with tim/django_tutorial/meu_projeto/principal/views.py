from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(response, id):  # não seria request? 
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse(f'<h1> {ls.name} </h1> <br> <h2> {item.text} </h2>')
