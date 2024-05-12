from django.shortcuts import render
from django.contrib import admin

def main(request):
    return render(request, 'modern-home-3.html')

def about(request):
    return render(request, 'about-modern.html')
