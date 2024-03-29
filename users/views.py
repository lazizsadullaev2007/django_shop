from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('store:home')
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:home')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'users/registration.html', context)


def user_logout(request):
    logout(request)
    return redirect('store:home')