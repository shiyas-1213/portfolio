from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request, 'portfolio_main.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'port_portfolio.html')