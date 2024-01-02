from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from users.forms import RegisterForm, LoginForm

# Create your views here.
def register_view(request):
    if request.method == "GET":
        context = {'form': RegisterForm,}

        return render(request, 'users/register.html', context=context)

    elif request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),

            )
            return redirect('/login/')

        else:
            context = {'form': form}

        return render(request, 'users/register.html', context=context)

def login_view(request):
    if request.method == 'GET':
        context = {'form': LoginForm,}
        return render(request, 'users/login.html', context=context)

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(**form.cleaned_data)

            if user is not None:
                login(request, user)
                return redirect('/')

            else:
                form.add_error(None, 'Неверный логин или пароль')

        return render(request, 'users/login.html', context={'form':form})


def logout_view(request):
    logout(request)
    return redirect('/')

def profile_view(request):
    if request.method == 'GET':
        context = {'user': request.user}
        return render(request, 'users/profile.html', context=context)

def delete_view(request):
    if request.method == 'GET':
        request.user.delete()
        return redirect('/')