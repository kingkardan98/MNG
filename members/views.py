from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Member
from .forms import MemberForm, MemberUpdateForm

# Create your views here.

def user_create_view(request):
    # The C in CRUD
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
    return render(request, 'member/create_user.html', context)

def create_success_view(request):
    return render(request, "member/create_success.html", {})

def user_detail_view(request, id):
    # The R in CRUD
    obj = get_object_or_404(Member, id=id)
    context = {
        "obj": obj
    }

    return render(request, "member/detail_user.html", context)

def update_user_view(request, id):
    # The U in CRUD
    obj = get_object_or_404(Member, id=id)
    data = {
        'availability': obj.availability,
        'spendable': obj.spendable,
        'username': obj.username,
        'email': obj.email,
        'password': obj.password,
        'confirm_password': obj.password
    }
    form = MemberUpdateForm(data)
    context = {
        "obj": obj,
        "form": form
    }

    return render(request, "member/update_user.html", context)

def updateuser(request, id):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    availability = request.POST['availability']
    spendable = request.POST['spendable']

    user = Member.objects.get(id=id)
    user.username = username
    user.email = email
    user.password = password
    user.availability = availability
    user.spendable = spendable
    user.save()

    context = {}

    return redirect(reverse('update_success_view', kwargs={'id': user.id}))

def update_success_view(request):
    return render(request, 'member/update_success.html', {})


def delete_user_view(request, id):
    # The D in CRUD
    obj = get_object_or_404(Member, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect(reverse('delete_success_view'))
    context = {
        "obj": obj
    }

    return render(request, "member/delete_user.html", context)

def delete_success_view(request):
    return render(request, 'member/delete_success.html', {})