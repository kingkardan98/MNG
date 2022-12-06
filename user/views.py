from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User
from .forms import UserForm

# Create your views here.

def user_create_view(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
            return redirect(reverse('create_success_view'))
    context = {
            "form": form
        }
    return render(request, 'user/create_user.html', context)

def user_detail_view(request):
    obj = User.objects.get(id=2)
    context = {
        "obj": obj
    }

    return render(request, "user/detail_user.html", context)

def create_success_view(request):
    return render(request, "user/create_success.html", {})