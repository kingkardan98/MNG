from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Member
from .forms import MemberForm

# Create your views here.

def member_create_view(request):
    # The C in CRUD - FULLY DONE
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
    # The R in CRUD - FULLY DONE
    obj = get_object_or_404(Member, username=username)
    context = {
        "obj": obj
    }

    return render(request, "member/detail_member.html", context)

def update_member_view(request, username):
    # The U in CRUD - WORK IN PROGRESS
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

def updatemember(request, username):
    memberName = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    availability = request.POST['availability']
    spendable = request.POST['spendable']

    user = Member.objects.get(username=username)
    user.username = memberName
    user.email = email
    user.password = password
    user.availability = availability
    user.spendable = spendable
    user.save()

    return redirect(reverse('update_success_view'))

def update_success_view(request):
    return render(request, 'member/update_success.html', {})


def delete_member_view(request, username):
    # The D in CRUD - FULLY DONE
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