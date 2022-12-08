from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import User
from .forms import UserForm

# Create your views here.

def user_create_view(request):
    # The C in CRUD
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

def create_success_view(request):
    return render(request, "user/create_success.html", {})

def user_detail_view(request, id):
    # The R in CRUD
    obj = get_object_or_404(User, id=id)
    context = {
        "obj": obj
    }

    return render(request, "user/detail_user.html", context)

def delete_user_view(request, id):
    # The D in CRUD
    obj = get_object_or_404(User, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect(reverse('delete_success_view'))
    context = {
        "obj": obj
    }

    return render(request, "user/delete_user.html", context)

def delete_success_view(request):
    return render(request, 'user/delete_success.html', {})