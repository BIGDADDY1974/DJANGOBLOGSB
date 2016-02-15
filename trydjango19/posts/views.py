from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def startup(request):
    return HttpResponse("<h1>THIS IS THE STARUP PAGE</h1>"
                        "<a href='http://127.0.0.1:8000/posts/'>Go to POSTS</a>")
def post_home(request):
    return HttpResponse("<h1>HELLO DJANGO BANGO</h1>")

def post_create(request):
    return HttpResponse("<h1>HELLO CREATE</h1>")

def post_detail(request):
    return HttpResponse("<h1>HELLO DETAIL</h1>")

def post_list(request):
    return HttpResponse("<h1>HELLO LIST</h1>")

def post_update(request):
    return HttpResponse("<h1>HELLO UPDATE</h1>")

def post_delete(request):
    return HttpResponse("<h1>HELLO DELETE</h1>")

