from django.urls import path

from estate_app.views import load_home_page

urlpatterns = [
    path('', load_home_page, name = 'load home page')
]