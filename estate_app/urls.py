from django.urls import path

from estate_app.views import load_home_page, about_us, general_rules, register, login

urlpatterns = [
    path('', load_home_page, name = 'load home page'),
    path('about/', about_us, name='load about us page'),
    path('general_rules/', general_rules, name='load general rules'),
    path('register/', register, name='load register page'),
    path('login/', login, name='load login page'),
]