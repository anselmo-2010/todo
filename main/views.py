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
    return render(request, "book.html", {"book_list": book_list})

def add_todo(request):
    form = request.POST 
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    text = form["book_text"]
    text2 = form["book_text2"]
    text3 = form["book_text3"]
    text4 = form["book_text4"]
    text5 = form["book_text5"]
    text6 = form["book_text6"]
    text7 = form["book_text7"]
    bookread = BookSale(title=text, author=text2, subtitle=text3, description=text4, year=text5, genre=text6, price=text7)
    bookread.save()
    return redirect(book_sale)
   
def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)

def book_delete(request, id):
    book = BookSale.objects.get(id=id)
    book.delete()
    return redirect(book_sale)

def book_todo(request, id):
    book = BookSale.objects.get(id=id)
    book.is_favorite = True
    book.save()
    return redirect(book_sale)

def book_detail(request, id):
    todo_object = BookSale.objects.filter(id=id)
    return render(request, "book.html", {"book_list": todo_object})