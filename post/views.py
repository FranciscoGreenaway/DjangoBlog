from django.contrib import auth, messages
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User, auth


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


def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "An account with that Username exists already")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "An account with that Email exists already")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match. Try again.")
            return redirect('signup')
    else:
        return render(request, 'signup.html')
