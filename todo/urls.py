"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name = "homepage"),
    path("test", test, name = "test"),
    path("page1", page1, name = "page1"),
    path("page2", page2, name = "page2"),
    path("page3", page3, name = "page3"),
    path("book", book_sale, name = "book"),
    path("add-todo", add_todo, name = "add-todo"),
    path("add-book", add_book, name = "add-book"),
    path("delete-todo/<id>/", delete_todo, name = "delete-todo"),
    path("mark-todo/<id>/", mark_todo, name = "mark-todo"),
    path("close-todo/<id>/", close_todo, name="close-todo"),
    path("book-todo/<id>/", book_todo, name = "book-todo"),
    path("book-delete/<id>/", book_delete, name = "book-delete"),
    path("book_detail/<id>/", book_detail, name = "book_detail",)
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
