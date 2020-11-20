from django.shortcuts import render

# Create your views here.
def load_home_page(request):
    return render(request, 'home_page.html')


def about_us(request):
    return render(request, 'about_us.html')


def general_rules(request):
    return render(request, 'general_rules.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')