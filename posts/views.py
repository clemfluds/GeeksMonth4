from django.shortcuts import render, HttpResponse
from random import randint
from posts.models import Post

def homepage_view(request):
    return render(request, "base.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/posts.html", context={"posts": posts})