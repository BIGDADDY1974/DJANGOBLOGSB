from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def startup(request):
    return HttpResponse("<h1>THIS IS THE STARTUP PAGE</h1>"
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

def post_detail(request,id=None):
    # instance = Post.objects.get(id=3)
    instance = get_object_or_404(Post,id=id)
    context = {
        "title":instance.title,
        "instance":instance
    }
    return render(request, 'post_detail.html', context)

def post_create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        print (form.cleaned_data.get("title"))
        instance.save()

    # if request.method == "POST":
    #     print (request.POST.get("content"))
    #     print (request.POST.get("title"))
    # Post.objects.create(title=title)
    # Post.objects.create(content=content)

    context = {
       "form":form,
    }
    return render(request, 'post_form.html', context)

def post_update(request):
    return HttpResponse("<h1>HELLO UPDATE</h1>")

def post_delete(request):
    return HttpResponse("<h1>HELLO DELETE</h1>")

