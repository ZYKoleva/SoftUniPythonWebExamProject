from django.urls import path

from estate_app.views import load_home_page, district, city, area, show_details, \
    create_add, AboutUsTemplateView, GeneralRulesTemplateView, approve_add, edit_add, delete_add, load_areas, \
    load_cities

urlpatterns = [
    path('', load_home_page, name='load home'),
    path('about/', AboutUsTemplateView.as_view(), name='load about us'),
    path('general_rules/', GeneralRulesTemplateView.as_view(), name='load general rules'),
    path('district/<int:pk>', district, name='load district'),
    path('city/<int:pk>', city, name='load city'),
    path('area/<int:pk>', area, name='load area'),
    path('details/<int:pk>/', show_details, name='show details'),
    path('create_add/', create_add, name='create ad'),
    path('approve_add/<int:pk>/', approve_add, name='approve add'),
    path('edit_add/<int:pk>/', edit_add, name='edit add'),
    path('delete_add/<int:pk>/', delete_add, name='delete add'),
    path('ajax_load_areas/', load_areas, name='load areas'),
    path('ajax_load_cities/', load_cities, name='load cities'),
]