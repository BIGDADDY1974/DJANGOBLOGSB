from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def startup(request):
    return HttpResponse("<h1>THIS IS THE STARUP PAGE</h1>"
                        "<a href='http://127.0.0.1:8000/posts/'>Go to POSTS</a>")

def post_home(request):
    return HttpResponse("<h1>HELLO DJANGO BANGO</h1>")
