from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book

def hello_view(request):
    if request.method == "GET":
        return HttpResponse("Hello This is my first project Django")


def blog_view(request):
    if request.method == "GET":
        book = Book.objects.all()
        return render(request, 'book.html', {'book': book})