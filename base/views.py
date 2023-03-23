from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.


class Index(View):
    def get(slef, request):
        return render(request, 'base/index.html')


class Home(View):
    def get(self, request):
        return render(request, 'base/home.html')


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        
        form = AuthenticationForm()
        return render(request, 'base/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')
        return render(request, 'base/login.html', {'form': form})


class Registration(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = SignUpForm()
        return render(request, 'base/registration.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.username = form.username.lower()
            form.save()
            messages.success(request, 'Registered Successfully! Login here.')
            return redirect('login')
        else:
            messages.error(
                request, 'Please fill the deatils correctly.')
        return redirect('registraion')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')
