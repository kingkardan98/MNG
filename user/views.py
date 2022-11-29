from django.shortcuts import render
from .models import User

# Create your views here.

def user_detail_view(request):
    obj = User.objects.get(id=1)
    context = {
        "Username": obj.username,
        "Email": obj.email,
        "Money availability": obj.moneyAvailability,
        "Spending limit": obj.spendingLimit
    }

    return render(request, "user/detail.html", context)