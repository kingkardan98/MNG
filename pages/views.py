from django.shortcuts import render

# Create your views here.

def choose_language_view(request):
    return render(request, "html/choose_language.html")

def home_view(request):
    return render(request, "html/en/home_view.html", {})

def contacts_view(request):
    mail_string = '<a href="mailto:fr.bambina@gmail.com"> fr.bambina@gmail.com </a>'
    link_string = '<a href="https://www.linkedin.com/in/francescobambina"> francescobambina </a>'

    contacts_dict = {"Email": mail_string, "Linkedin": link_string}
    context = {
        "contacts_text": "Contact information",
        "contacts_dict": contacts_dict
    }
    return render(request, "html/en/contacts_view.html", context)

def about_view(request):
    context = {
        "about": "This website is a small project created by me as a presentation for a job interview.",
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
    mail_string = '<a href="mailto:fr.bambina@gmail.com"> fr.bambina@gmail.com </a>'
    link_string = '<a href="https://www.linkedin.com/in/francescobambina"> francescobambina </a>'

    contacts_dict = {"Email": mail_string, "Linkedin": link_string}
    context = {
        "contacts_text": "Contatti",
        "contacts_dict": contacts_dict
    }
    return render(request, "html/it/contacts_view_it.html", context)

def about_view_it(request):
    context = {
        "about": "Questo sito internet è un piccolo progetto creato da me come presentazione per un'offerta di lavoro.",
    }

    return render(request, "html/it/about_view_it.html", context)

def refused_it(request):
    return render(request, 'html/it/refused_it.html', {}, status=401)