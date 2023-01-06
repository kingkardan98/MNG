from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return render(request, "html/home_view.html", {})

def contacts_view(request):
    context = {
        "contacts_text": "Contact information",
        "contacts_dict": {"mary": "123", "jackson": "000", "meeseeks": "4446064447777833777063377773333557777"} 
    }
    return render(request, "html/contacts_view.html", context)

def about_view(request):
    context = {
        "about": "This website is a small project created by me as a presentation for a job interview.",
        "email": "mail@mailservice.com",
        "phone": "123 4567890"
    }

    return render(request, "html/about_view.html", context)

def refused(request):
    return render(request, 'html/refused.html', {}, status=401)

# ----------------------------- ITALIAN -----------------------------

def home_view_it(request):
    return render(request, "html/home_view_it.html", {})

def contacts_view_it(request):
    context = {
        "contacts_text": "Contatti",
        "contacts_dict": {"mary": "123", "jackson": "000", "meeseeks": "4446064447777833777063377773333557777"} 
    }
    return render(request, "html/contacts_view.html_it", context)

def about_view_it(request):
    context = {
        "about": "Questo sito internet è un piccolo progetto creato da me come presentazione per un'offerta di lavoro.",
        "email": "mail@mailservice.com",
        "phone": "123 4567890"
    }

    return render(request, "html/about_view_it.html", context)

def refused_it(request):
    return render(request, 'html/refused_it.html', {}, status=401)