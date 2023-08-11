from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
from . models import *

# Create your views here.
def allblogs(request):
    all_posts = Post.objects.all()
    if request.method == "GET":
        query = request.GET.get("q")
        queryset = Q(title__icontains=query)|Q(intro__icontains=query)
        if query:
            result = Post.objects.filter(queryset) 
        else:
            result = all_posts
    context = {'all_posts':all_posts,
               'query':query,
               'queryset':queryset,
               'all_posts':all_posts,
               'result':result
               }
    return render(request,'blogApp/list.html',context)

def detail(request,pk):
    all_posts = Post.objects.all()
    ten_post = Post.objects.all()[:10]
    detail_post = Post.objects.get(pk=pk)
    detail_more_post = More_post.objects.filter(post=detail_post)
    comment_post = Comment.objects.filter(post=detail_post)
    count_comment = comment_post.count
    context={'all_posts':all_posts,
             'detail_more_post':detail_more_post,
             'ten_post':ten_post,
             'comment_post':comment_post,
             'count_comment':count_comment,
             'detail_post':detail_post}
    if request.method == "POST":
        if request.user.is_authenticated:
            email = request.user.email
        else:
            email = request.POST.get('email')
        comment_text = request.POST.get('comment_text')
        if (email!="" and comment_text!=""):
            Comment.objects.create(email=email, comment_text=comment_text,post=detail_post)
            messages.success(request,'thanks for the comment')
    return render(request,'blogApp/detail.html',context)
