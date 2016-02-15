from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def startup(request):
    return HttpResponse("<h1>THIS IS THE STARUP PAGE</h1>"
                        "<a href='http://127.0.0.1:8000/posts/'>Go to POSTS</a>")
def post_home(request):
    context = {
       "title":"HOME"
    }
    return render(request, 'index.html', context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list":queryset,
        "title":"List"
    }
    # if request.user.is_authenticated():
    #     context = {
    #    "title":"USER AUTHENTICATED"
    # }
    # else:
    #     context = {
    #    "title":"USER NOT AUTHENTICATED"
    # }
    return render(request, 'index.html', context)

def post_create(request):
    context = {
       "title":"Create"
    }
    return render(request, 'index.html', context)

def post_detail(request):
    context = {
        "title":"Detail"
    }
    return render(request, 'index.html', context)

def post_update(request):
    return HttpResponse("<h1>HELLO UPDATE</h1>")

def post_delete(request):
    return HttpResponse("<h1>HELLO DELETE</h1>")

