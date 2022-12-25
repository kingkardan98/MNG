from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm  

# Create your views here.

def login_user(request):
    request.session['logged_user'] = ''
    context = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['logged_user'] = username
            return redirect('member_list_view', logged_user=username)

        else:
            messages.success(request, ("There was an error logging in."))
            return render(request, 'userAuth/login.html', context)
            
    else:
        return render(request, 'userAuth/login.html', context)

def logout_user(request):
    context = {
        "username": request.user.username
    }
    logout(request)
    return render(request, 'userAuth/logout.html', context)

def create_user_view(request):
    form = UserCreationForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created succesfully!")

            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('member_list_view', logged_user=request.user)
        
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }

    return render(request, 'userAuth/create_user.html', context)