from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.todo_list, name="todo_list"),
    path("create/", views.create, name="create")
]
