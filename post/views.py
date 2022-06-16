from django.contrib import auth, messages
from django.shortcuts import render, redirect
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})


def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Incorrect Username or Password")
            return redirect('login')
    else:
        return render(request, 'login.html')

