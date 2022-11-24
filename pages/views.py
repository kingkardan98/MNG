from django.shortcuts import render
from django.http import HttpResponse
from utils import read_html

# Create your views here.

def home_view(request):
    html = read_html('home_view.html')
    return render(request, "html_views/home_view.html", {})

def contacts_view(request):
    html = read_html('contacts_view.html')
    return HttpResponse(html, status=200)