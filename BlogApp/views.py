from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from MyProject.forms import New_Blog
from django.template.defaulttags import register
from .models import Blog

# Create your views here.

@register.filter
def get_author(author_id):
    usr = User.objects.filter(id = author_id).first()
    return usr.first_name

@login_required
def home(request):
    users = User.objects.all()
    Blogs = Blog.objects.all().order_by('-date_posted').values()
    return render(request, 'home.html', {'blogs': Blogs, 'users': users})
    
@login_required
def new_blog(request):
    if request.method == "POST":
        form = New_Blog(request.POST)
        usr = User.objects.get(username = request.user.username)
        if form.is_valid():
            new = Blog.objects.create(
                title = form.cleaned_data.get("title").title(),
                content = form.cleaned_data.get("content"),
                author = usr
            )
            new.save()
            return render(request, "new_blog_done.html", {})
    else:
        form = New_Blog()
        return render(request, "new_blog.html", {'form': form})
        
@login_required
def view_profile(request):
    usr = User.objects.filter(username = request.user.username).first()
    blogs = usr.blog_set.all().order_by('-date_posted').values()
    return render(request, 'profile.html', {'blogs': blogs})
    
@login_required
def edit_blog(request, blog_id):
    if request.method == "POST":
        blog = Blog.objects.filter(id = blog_id).first()
        form = New_Blog(request.POST)        
        if form.is_valid():
            blog.title = form.cleaned_data.get("title").title()
            blog.content = form.cleaned_data.get("content")
            blog.save()
            return render(request, "edit_blog_done.html", {})
    else:
        blog = Blog.objects.filter(id = blog_id).first()
        initial_data = {'title': blog.title, 'content': blog.content}
        form = New_Blog(initial = initial_data)
        return render(request, "edit_blog.html", {'form': form, 'blog_id': blog_id})
    
@login_required
def delete_blog(request, blog_id):
    blog = Blog.objects.filter(id = blog_id).first()
    blog.delete()
    usr = User.objects.filter(username = request.user.username).first()
    blogs = usr.blog_set.all().order_by('-date_posted').values()
    return render(request, "profile.html", {'blogs': blogs})