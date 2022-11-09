from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import User, Post, Comments
from .forms import PostForm


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exists!')
            return redirect('home')
        

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')
            

    return render(request, 'home/login.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    posts = Post.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
    return render(request, 'home/home.html', {'posts' : posts})

@login_required(login_url='login')
def post(request, pid):
    post = Post.objects.get(id=pid)
    return render(request, 'home/post.html', {'post' : post})


@login_required(login_url='login')
def newPost(request):
    if request.user.is_staff == False:
        return HttpResponse('You cannot Post')

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    return render(request, 'home/post_form.html', {'form' : form})


@login_required(login_url='login')
def updatePost(request, pid):
    if request.user.is_staff == False:
        return HttpResponse('You are not authorized to edit this post')

    post = Post.objects.get(id=pid)
    form = PostForm(instance=post)

    if request.user != post.author:
        return HttpResponse('You are not authorized to edit this post')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'home/post_form.html', {'form' : form})


@login_required(login_url='login')
def deletePost(request, pid):
    if request.user.is_staff == False:
        return HttpResponse('You cannot Delete')

    post = Post.objects.get(id=pid)
    
    if request.user != post.author:
        return HttpResponse('You are not authorized to delete this post')

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'home/delete.html', {'obj' : post})



# Create your views here.

