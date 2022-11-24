from django.shortcuts import render
from django.http import HttpResponse
from utils import read_html

# Create your views here.

def home_view(request):
    return render(request, "home_view.html", {})

def contacts_view(request):
    return render(request, "contacts_view.html", {})