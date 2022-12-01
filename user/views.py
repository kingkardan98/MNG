from django.shortcuts import render
from .models import User
from .forms import UserForm

# Create your views here.

def user_create_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()
    context = {
        'form': form
    }

    return render(request, 'user/create_user.html', context)

def user_detail_view(request):
    obj = User.objects.get(id=1)
    context = {
        "obj": obj
    }

    return render(request, "user/detail_user.html", context)