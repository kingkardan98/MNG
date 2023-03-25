from django.shortcuts import render

# Create your views here.

def choose_language_view(request):
    return render(request, "html/choose_language.html")

def home_view(request):
    return render(request, "html/en/home_view.html", {})

def contacts_view(request):
    contacts_dict = {"Email": "fr.bambina@gmail.com", "Linkedin": ""}
    context = {
        "contacts_text": "Contact information",
        "contacts_dict": contacts_dict
    }
    return render(request, "html/en/contacts_view.html", context)

def about_view(request):
    context = {
        "about": "This website is a small project created by me as a presentation for a job interview.",
        "email": "fr.bambina@gmail.com",
        "phone": "Write me an email to get in contact with me through the phone!"
    }

    return render(request, "html/en/about_view.html", context)

def refused(request):
    return render(request, 'html/en/refused.html', {}, status=401)

# ----------------------------- ITALIAN -----------------------------
# -----------------------------  AHEAD  -----------------------------
# -----------------------------  TREAD  -----------------------------
# --------------------------- PASTAFULLY ----------------------------

def home_view_it(request):
    return render(request, "html/it/home_view_it.html", {})

def contacts_view_it(request):
    contacts_dict = {"Email": "fr.bambina@gmail.com", "Linkedin": ""}
    context = {
        "contacts_text": "Contatti",
        "contacts_dict": contacts_dict
    }
    return render(request, "html/it/contacts_view_it.html", context)

def about_view_it(request):
    context = {
        "about": "Questo sito internet è un piccolo progetto creato da me come presentazione per un'offerta di lavoro.",
        "email": "fr.bambina@gmail.com",
        "phone": "Scrivimi un'email per metterti in contatto telefonicamente!"
    }

    return render(request, "html/it/about_view_it.html", context)

def refused_it(request):
    return render(request, 'html/it/refused_it.html', {}, status=401)