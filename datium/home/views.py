from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
# Create your views here.

def index(request):
    # Page from the theme 
    return render(request, 'pages/dashboard.html')
def aboutus(request):
    return render(request, 'pages/aboutus.html')
def profile(request):
    return render(request, 'pages/profile.html')
def contact(request):
    if request.method == 'POST':
        contact = Contact(
            name = request.POST.get('name'),
            email=request.POST.get('email'),
            number=request.POST.get('number'),
            message=request.POST.get('message')
        )      
        contact.save()
        success = True
        return render(request, 'pages/contact.html', {
            'success': success
        })
    return render(request, 'pages/contact.html')
def services(request):
    return render(request, 'pages/tables.html')
def privacy(request):
    return render(request, 'pages/privacy.html')
def terms(request):
    return render(request, 'pages/terms.html')

