# Create your views here.
from django.shortcuts import render, HttpResponse

from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    return render(request, "user_list.html")

def user_add(request):
    return render(request, 'user_add.html')

def tpl(request):
    name ="罗想"
    roles = ["司机","CEO","保安"]
    user_info ={"name": "燕凌尔", "salary": 1000000000, "role": "前座"}

    data_list = [
        {"name": "丛薪航", "salary": 1000000000, "role": "后座1"},

        {"name": "陈星语", "salary": 1000000000, "role": "后座2"},
    ]

    return render(request, 'tpl.html', {"n1": name,"n2": roles,'n3': user_info, "n4": data_list})