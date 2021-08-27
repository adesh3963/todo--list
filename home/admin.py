from django.contrib import admin

# Register your models here.
from home.models import ToDoList

admin.site.register(ToDoList)