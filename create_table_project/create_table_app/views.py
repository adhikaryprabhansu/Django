from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def show_message(request):
#     return HttpResponse("<h1>Hello World</h1>")

def home_page(request):
    return render(request, 'home.html') 

def about_page(request):
    return render(request, 'about.html') 
