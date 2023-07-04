from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('authors_sellers')
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


def authors_sellers(request):
    users = CustomUser.objects.filter(public_visibility=True)
    return render(request, 'user/authors_sellers.html', {'users': users})
