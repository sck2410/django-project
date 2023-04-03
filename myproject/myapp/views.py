from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *

# Create your views here.
def index(request):
    students = student.objects.all()
    return render(request, "index.html", {"students":students})

def about(request):
    return render(request, "about.html")

def form(request):
    return render(request, "form.html")