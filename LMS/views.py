from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, get_user_model
from datetime import date, timezone
from datetime import date
from django.contrib.auth.decorators import login_required
User = get_user_model()

from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


# Create your views here.
def Welcome (request):
    return render(request, 'base.html')


def contact (request):
    return render(request, 'contact.html')

def about (request):
    return render(request, 'about.html')




def signup(request):
    if not request.user.is_anonymous:
        return redirect("/")
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not name or not email or not password:
            messages.error(request, 'Please fill out all the fields.')
            return render(request, 'signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already signed up. Head to the login page.')
            return render(request, 'signup.html')
        
        if User.objects.filter(username=name).exists():
            messages.error(request, 'Username already taken. Please try something else.')
            return render(request, 'signup.html')
        
        user = User.objects.create_user(username=name, email=email, first_name=name, password=password)
        messages.success(request, f'Your account is created, {name}. Head to the login page!')
        return redirect('signin')  
    
    return render(request, 'signup.html')

def user_logout(request):
    logout(request)

    return redirect('/')  # Change 'Welcome' to the appropriate view name or URL pattern

def signin(request):
    if not request.user.is_anonymous:
        return redirect('/') 

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)  # Log in the user
            messages.success(request, f'Welcome back, {username}!')
            return redirect('/')
        else:
            messages.error(request, 'Wrong username or password')
    return render(request, 'signin.html')

