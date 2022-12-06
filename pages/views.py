from django.shortcuts import render

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