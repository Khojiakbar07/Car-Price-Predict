from django.shortcuts import render
from django.contrib import admin

def main(request):
    return render(request, 'electro-home.html')

def about(request):
    return render(request, 'about-modern.html')

def service(request):
    return render(request, 'services-modern.html')

def carpredict(request):
    if request.method=="POST":
        print (request.POST.get('Carname'))
        print (request.POST.get('model'))
    return render(request, 'car-details.html')

def carlisting(request):
    return render(request, 'car-listing.html')

def contact(request):
    return render(request, 'contact-modern.html')

def login(request):
    return render(request, 'Login.html')
