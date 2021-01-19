from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import BookSale

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

def book_sale(request):
    book_list = BookSale.objects.all()
    return render(request, "books.html", {"book_list": book_list})

def add_todo(request):
    form = request.POST 
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)