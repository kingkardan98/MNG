from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Member
from .forms import MemberForm

# Create your views here.

def member_create_view(request):
    # The C in CRUD - FULLY WORKS

    logged_user = request.user

    form = MemberForm(initial={'author': logged_user})

    if request.method == "POST":
        form = MemberForm(data=request.POST, initial={'author': logged_user})
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = logged_user
            obj.save()
            return redirect(reverse('create_success_view'))
    context = {
            "form": form
        }
    return render(request, 'member/create_member.html', context)

def create_success_view(request):
    return render(request, "member/create_success.html", {})

def member_list_view(request, logged_user):
    memberList = list(Member.objects.filter(author = logged_user))
    obj = Member.objects.filter(author = logged_user).first()

    if str(request.user) != obj.author:
        return redirect(reverse('refused'))
        

    context = {
        "memberList": memberList,
        "logged_user": logged_user
    }

    return render(request, 'member/member_list.html', context)

def member_detail_view(request, name):
    # The R in CRUD - FULLY WORKS

    obj = get_object_or_404(Member, name=name)

    if str(request.user) != obj.author:
        return redirect(reverse('refused'))

    context = {
        "obj": obj
    }

    return render(request, "member/detail_member.html", context)

def update_member_view(request, name):
    # The U in CRUD - FULLY WORKS

    logged_user = request.user
    obj = get_object_or_404(Member, name=name)

    if str(logged_user) != str(obj.author):
        return redirect(reverse('refused'))

    member_form = MemberForm(instance=obj, initial={'author': logged_user})

    if request.method == "POST":
        member_form = MemberForm(request.POST, instance=obj, initial={'author': logged_user})
        if member_form.is_valid():
            member_form.save()
            return redirect(reverse('update_success_view'))

    context = {
        "obj": obj,
        "member_form": member_form
    }

    return render(request, "member/update_member.html", context)

def update_success_view(request):
    return render(request, 'member/update_success.html', {})


def delete_member_view(request, name):
    # The D in CRUD - FULLY WORKS
    
    obj = get_object_or_404(Member, name=name)

    if str(request.user) != obj.author:
        return redirect(reverse('refused')) 

    if request.method == "POST":
        obj.delete()
        return redirect(reverse('delete_success_view'))
    context = {
        "obj": obj
    }

    return render(request, "member/delete_member.html", context)

def delete_success_view(request):
    return render(request, 'member/delete_success.html', {})