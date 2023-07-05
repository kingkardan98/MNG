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
    description = """
    This website is a small project created by me as a presentation for a job interview.
    It is (even though it's a tiny website) a labor of love.
    I've learned to use some technologies through this development project.
    The website's backend is fully written in Python, and it uses a lightweight SQLite3 database.
    Resource routing, HTTP responses and database operations are all managed using the Django framework.
    Basic HTML is used to render the website, with some CSS and JavaScript styling.
    """

    context = {
        "about": description,
    }

    return render(request, "html/en/about_view.html", context)

def refused(request):
    return render(request, 'html/en/refused.html', {}, status=401)

def documentation_view(request):
    return render(request, 'html/documentation.html', {})

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
    description = """
    Questo sito è un piccolo progetto creato da me come presentazione per un possibile colloquio di lavoro.
    Per quanto piccolo, è un progetto nato dall'amore per la programmazione.
    Ho imparato le tecnologie richieste attraverso lo sviluppo di questo progetto.
    Il backend del sito è scritto interamente in Python, e utilizza un database leggero SQlite3.
    Resource routing, chiamate HTTP e operazioni sul database sono gestite tramite il framework Django.
    HTML di base, CSS e JavaScripti sono utilizzati per la parte grafica del sito.
    """

    context = {
        "about": description,
    }

    return render(request, "html/it/about_view_it.html", context)

def refused_it(request):
    return render(request, 'html/it/refused_it.html', {}, status=401)