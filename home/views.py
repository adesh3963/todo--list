from django.http import request
from django.shortcuts import render,HttpResponse
from home.models import ToDoList
# Create your views here.
def todo(request):
    context={"success":False}
    if request.method=="POST":
        print("data coming")
        
        task_discrip=request.POST["task_discrip"]
        title= request.POST["title"]
        class_obj=ToDoList(titletext=title,textdiscrip=task_discrip)
        class_obj.save()
        print("form accepted")
        context={"success":True}
 
    return render(request,"todo.html",context)
def task(request):
    alltask=ToDoList.objects.all()
    context={"task":alltask}
    return render(request,"task.html",context)
