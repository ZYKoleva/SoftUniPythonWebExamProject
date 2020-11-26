from django.urls import path

from estate_app.views import load_home_page, about_us, general_rules, district, city, area, show_details, looking_for

urlpatterns = [
    path('', load_home_page, name='load home'),
    path('about/', about_us, name='load about us'),
    path('general_rules/', general_rules, name='load general rules'),
    path('district/<int:pk>', district, name='load district'),
    path('city/<int:pk>', city, name='load city'),
    path('area/<int:pk>', area, name='load area'),
    path('details/<int:pk>/', show_details, name='show details'),
    path('looking_for/', looking_for, name='looking for')
]