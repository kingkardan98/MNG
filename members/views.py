from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Member
from .forms import MemberForm
from .admin import MemberHistoryAdmin

from .edit_parse import operationEnToIt

import pytz

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
    return render(request, "member/create_success.html")

def member_list_view(request, logged_user):
    memberList = list(Member.objects.filter(author = logged_user))
    obj = Member.objects.filter(author = logged_user).first()

    if str(request.user) != logged_user:
        return redirect(reverse('refused'))

    if obj == None:
        context = {}
        return render(request, 'member/member_list.html', context)
        

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

def member_history_list_view(request, name):
    obj = get_object_or_404(Member, name=name)

    if str(request.user) != obj.author:
        return redirect(reverse('refused'))

    history = {}
    obj_history = obj.history.all()

    for e in obj_history:
        operation = MemberHistoryAdmin.list_changes(MemberHistoryAdmin, e)
        timestamp = MemberHistoryAdmin.get_datetime(MemberHistoryAdmin, e)
        if operation != None:
            history[operation] = timestamp

    context = {
        'obj': obj,
        'history': history,
    }

    return render(request, 'member/member_history_list.html', context)

def update_member_view(request, name):
    # The U in CRUD - FULLY WORKS

    logged_user = request.user
    obj = get_object_or_404(Member, name=name)
    old_obj = get_object_or_404(Member, name=name)

    if str(logged_user) != str(obj.author):
        return redirect(reverse('refused'))

    member_form = MemberForm(instance=obj, initial={'author': logged_user})

    if request.method == "POST":
        member_form = MemberForm(request.POST, instance=obj, initial={'author': logged_user})
        if member_form.is_valid() and member_form.errors == {}:
            member_form.save()
            return redirect(reverse('update_success_view'))

    context = {
        "old_obj": old_obj,
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

def user_delete_cleaner_function(user_members):
    for obj in user_members:
        obj.delete()

# ----------------------------- ITALIAN -----------------------------

def member_create_view_it(request):
    # The C in CRUD - FULLY WORKS

    logged_user = request.user

    form = MemberForm(initial={'author': logged_user})

    field_names = ['Disponibilità', 'Limite di spesa', 'Nome', 'Email', 'Utente']

    form.fields['availability'].widget.attrs['placeholder'] = 'Disponibilità'
    form.fields['spendable'].widget.attrs['placeholder'] = 'Limite di spesa'
    form.fields['name'].widget.attrs['placeholder'] = 'Nome'
    form.fields['author'].widget.attrs['placeholder'] = 'Utente'

    if request.method == "POST":
        form = MemberForm(data=request.POST, initial={'author': logged_user})
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = logged_user
            obj.save()
            return redirect(reverse('create_success_view_it'))
    context = {
            "form": form,
            "field_names": field_names
        }
    return render(request, 'member/create_member_it.html', context)

def create_success_view_it(request):
    return render(request, "member/create_success_it.html")

def member_list_view_it(request, logged_user):
    memberList = list(Member.objects.filter(author = logged_user))
    obj = Member.objects.filter(author = logged_user).first()

    if str(request.user) != logged_user:
        return redirect(reverse('refused_it'))

    if obj == None:
        context = {}
        return render(request, 'member/member_list_it.html', context)
        

    context = {
        "memberList": memberList,
        "logged_user": logged_user
    }

    return render(request, 'member/member_list_it.html', context)

def member_detail_view_it(request, name):
    # The R in CRUD - FULLY WORKS

    obj = get_object_or_404(Member, name=name)

    if str(request.user) != obj.author:
        return redirect(reverse('refused_it'))

    context = {
        "obj": obj
    }

    return render(request, "member/detail_member_it.html", context)

def member_history_list_view_it(request, name):
    obj = get_object_or_404(Member, name=name)

    if str(request.user) != obj.author:
        return redirect(reverse('refused_it'))

    history = {}
    obj_history = obj.history.all()

    for e in obj_history:
        operation = MemberHistoryAdmin.list_changes(MemberHistoryAdmin, e)

        if operation != None:
            operation = operationEnToIt(operation)

            timestamp = MemberHistoryAdmin.get_datetime(MemberHistoryAdmin, e)
            timestamp = timestamp.astimezone(pytz.timezone('Europe/Rome')).strftime("%d/%m/%Y, %H:%M:%S")
            history[operation] = timestamp

    context = {
        'obj': obj,
        'history': history,
    }

    return render(request, 'member/member_history_list_it.html', context)

def update_member_view_it(request, name):
    # The U in CRUD - FULLY WORKS

    logged_user = request.user
    obj = get_object_or_404(Member, name=name)
    old_obj = get_object_or_404(Member, name=name)

    if str(logged_user) != str(obj.author):
        return redirect(reverse('refused'))

    member_form = MemberForm(instance=obj, initial={'author': logged_user})

    if request.method == "POST":
        member_form = MemberForm(request.POST, instance=obj, initial={'author': logged_user})
        if member_form.is_valid():
            member_form.save()
            return redirect(reverse('update_success_view_it'))

    context = {
        "obj": obj,
        "old_obj": old_obj,
        "member_form": member_form
    }

    return render(request, "member/update_member_it.html", context)

def update_success_view_it(request):
    return render(request, 'member/update_success_it.html', {})


def delete_member_view_it(request, name):
    # The D in CRUD - FULLY WORKS
    
    obj = get_object_or_404(Member, name=name)

    if str(request.user) != obj.author:
        return redirect(reverse('refused_it')) 

    if request.method == "POST":
        obj.delete()
        return redirect(reverse('delete_success_view_it'))
    context = {
        "obj": obj
    }

    return render(request, "member/delete_member_it.html", context)

def delete_success_view_it(request):
    return render(request, 'member/delete_success_it.html', {})