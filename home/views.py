from django.shortcuts import render
from django.contrib import admin

def main(request):
    return render(request, 'modern-home-3.html')

def about(request):
    return render(request, 'about-modern.html')

def carpredict(request):
    return render(request, 'car-details.html')

def carlisting(request):
    return render(request, 'car-listing.html')

def contact(request):
    return render(request, 'contact-modern.html')