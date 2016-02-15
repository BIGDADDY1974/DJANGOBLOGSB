from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

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
        messages.success(request,"Sucsesfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"NOT Sucsesfully Created")
    # if request.method == "POST":
    #     print (request.POST.get("content"))
    #     print (request.POST.get("title"))
    # Post.objects.create(title=title)
    # Post.objects.create(content=content)
    context = {
         "form":form,
        }
    return render(request, 'post_form.html', context)

def post_update(request, id=None):
    instance = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title":instance.title,
        "instance":instance,
        "form":form,
    }
    return render(request, 'post_form.html', context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:list")

