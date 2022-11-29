from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return render(request, "home_view.html", {})

def contacts_view(request):
    context = {
        "contacts_text": "Contact information",
        "contacts_dict": {"mary": "123", "jackson": "000", "meeseeks": "4446064447777833777063377773333557777"} 
    }
    return render(request, "contacts_view.html", context)