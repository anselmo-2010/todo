from django.shortcuts import render, HttpResponse
from .models import ToDo

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def page1(request):
    return render(request, "page1.html")   

def page2(request):
    return render(request, "page2.html")  

def page3(request):
    return render(request, "page3.html") 