
from django.shortcuts import render

# Create your views here.

def members(response):
    return render(response, "student.html", {})