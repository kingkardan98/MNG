from django.shortcuts import render
from .models import User

# Create your views here.

def user_detail_view(request):
    obj = User.objects.get(id=1)
    context = {
        "username": obj.username,
        "email": obj.email,
        "availability": obj.availability,
        "spendingLimit": obj.spendingLimit,
    }

    return render(request, "user/detail.html", context)