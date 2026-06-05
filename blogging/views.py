from blogging.models import Post
from blogging.forms import PostForm
from django.shortcuts import render,redirect


def home(request):
 posts = Post.objects.all()
 return render(request, "index.html",{"posts": posts})

def post_creation(request):
 if request.method =="POST":
  form = PostForm(request.POST)
  if form.is_valid():
   form.save()
   return redirect ("home")
 else: 
    form = PostForm()
 return render(request,"index.html",{"form": form})

def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm(instance=post)
    return render(request, "edit.html", {"form": form})

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return redirect("home")#return response("post deleted") 
