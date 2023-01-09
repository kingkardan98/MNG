from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from members.models import Member

from members.views import user_delete_cleaner_function

# Create your views here.

def login_user(request):
    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass

    request.session['logged_user'] = ''
    context = {}

    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass
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
            return render(request, 'userAuth/en/login.html', context)
            
    else:
        return render(request, 'userAuth/en/login.html', context)

def logout_user(request):
    context = {
        "username": request.user.username
    }
    logout(request)
    return render(request, 'userAuth/en/logout.html', context)

def create_user_view(request):

    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass
    
    form = UserCreationForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        possible_user = User.objects.filter(username=request.POST['username'])
        if possible_user:
            messages.success(request, 'User already existing, use another username.')
            form = UserCreationForm()
        else:
            pass

        if form.is_valid():
            form.save()
            messages.success(request, "User created succesfully!")

            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('member_list_view', logged_user=request.user)

        return render(request, 'userAuth/en/create_user.html', context)
        
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }

    return render(request, 'userAuth/en/create_user.html', context)

def delete_user(request):
    username = request.user
    u = User.objects.get(username=username)
    user_members = list(Member.objects.filter(author=username))

    context = {
        'username': username,
        'err': None,
        'user_members': user_members,
    }

    if len(user_members) != 0:
        obj = user_members[0]
        context['obj'] = obj

    if str(request.user) != str(username):
        return redirect(reverse('refused'))

    else:
        if request.method == 'POST':
            user_delete_cleaner_function(user_members=user_members)
            u.delete()
            return redirect(reverse('user_delete_success_view'))

    return render(request, 'userAuth/en/delete_user.html', context)

def user_delete_success_view(request):
    context = {}
    return render(request, 'userAuth/en/delete_success.html', context)

# ----------------------------- ITALIAN -----------------------------
# -----------------------------  AHEAD  -----------------------------
# -----------------------------  TREAD  -----------------------------
# --------------------------- PASTAFULLY ----------------------------

def login_user_it(request):
    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass

    request.session['logged_user'] = ''
    context = {}

    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['logged_user'] = username
            return redirect('member_list_view', logged_user=username)

        else:
            messages.success(request, ("C'è stato un errore nell'accesso."))
            return render(request, 'userAuth/it/login_it.html', context)
            
    else:
        return render(request, 'userAuth/it/login_it.html', context)

def logout_user_it(request):
    context = {
        "username": request.user.username
    }
    logout(request)
    return render(request, 'userAuth/it/logout_it.html', context)

def create_user_view_it(request):
    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass

    form = UserCreationForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        possible_user = User.objects.filter(username=request.POST['username'])
        if possible_user:
            messages.success(request, 'Utente già registrato, usare un altro nome utente.')
        if form.is_valid():
            form.save()
            messages.success(request, "Utente creato con successo!")

            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('member_list_view_it', logged_user=request.user)
        
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }

    return render(request, 'userAuth/it/create_user_it.html', context)

def delete_user_it(request):
    username = request.user
    u = User.objects.get(username=username)
    user_members = list(Member.objects.filter(author=username))

    context = {
        'username': username,
        'err': None,
        'user_members': user_members,
    }

    if len(user_members) != 0:
        obj = user_members[0]
        context['obj'] = obj

    if str(request.user) != str(username):
        return redirect(reverse('refused_it'))

    else:
        if request.method == 'POST':
            user_delete_cleaner_function(user_members=user_members)
            u.delete()
            return redirect(reverse('user_delete_success_view_it'))

    return render(request, 'userAuth/it/delete_user_it.html', context)

def user_delete_success_view_it(request):
    context = {}
    return render(request, 'userAuth/it/delete_success_it.html', context)