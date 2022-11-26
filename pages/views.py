from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return render(request, "home_view.html", {})

def contacts_view(request):
    context = {
        "contacts_text": "Contact information"
    }
    return render(request, "contacts_view.html", context)