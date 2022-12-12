from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from members.views import member_detail_view
from members.models import Member

# Create your views here.

def login_user(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            obj = get_object_or_404(Member, username=username)
            print(obj.id)
            return redirect(reverse('user_detail_view'), args=[obj.id])

        else:
            # Return an 'invalid login' error message.
            print("Error")
            pass
            
    else:
        return render(request, 'userAuth/login.html', context)