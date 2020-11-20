from django.shortcuts import render

# Create your views here.
def load_home_page(request):
    return render(request, 'home_page.html')