from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):  # não seria request? 
    return HttpResponse('<h1>Olá, mundo!</h1>')

def adeus(response):
    return HttpResponse('<h1>Adeus, mundo!</h1>')
