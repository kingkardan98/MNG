from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Member
from .forms import MemberForm

# Create your views here.

def member_create_view(request):
    # The C in CRUD - FULLY WORKS
    # Will need to implement the capability to access it only
    # while logged in into the specific user. No other users
    # should be accessible. With this view the User in the
    # admin site should be created too.

    form = MemberForm()
    if request.method == "POST":
        form = MemberForm(data=request.POST)
        if form.is_valid():
            form.save()
            form = MemberForm()
            return redirect(reverse('create_success_view'))
    context = {
            "form": form
        }
    return render(request, 'member/create_member.html', context)

def create_success_view(request):
    return render(request, "member/create_success.html", {})

def member_detail_view(request, username):
    # The R in CRUD - FULLY WORKS
    # Will need to implement the capability to access it only
    # while logged in into the specific user. No other users
    # should be accessible.

    obj = get_object_or_404(Member, username=username)
    context = {
        "obj": obj
    }

    return render(request, "member/detail_member.html", context)

def update_member_view(request, username):
    # The U in CRUD - FULLY WORKS
    # Will need to implement the capability to access it only
    # while logged in into the specific user. No other users
    # should be accessible. With this view the User in the
    # admin site should be updated too.

    obj = get_object_or_404(Member, username=username)
    form = MemberForm(instance=obj)

    if request.method == "POST":
        form = MemberForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('update_success_view'))

    context = {
        "obj": obj,
        "form": form
    }

    return render(request, "member/update_member.html", context)

def update_success_view(request):
    return render(request, 'member/update_success.html', {})


def delete_member_view(request, username):
    # The D in CRUD - FULLY WORKS
    # Will need to implement the capability to access it only
    # while logged in into the specific user. No other users
    # should be accessible. With this view the User in the
    # admin site should be deleted too.
    
    obj = get_object_or_404(Member, username=username)
    if request.method == "POST":
        obj.delete()
        return redirect(reverse('delete_success_view'))
    context = {
        "obj": obj
    }

    return render(request, "member/delete_member.html", context)

def delete_success_view(request):
    return render(request, 'member/delete_success.html', {})