from django.urls import path

from estate_app.views import load_home_page, district, city, area, show_details, \
    create_ad, AboutUsTemplateView, GeneralRulesTemplateView, approve_ad, edit_ad, delete_ad, load_areas, \
    load_cities, reject_ad, AdListApiView

urlpatterns = [
    path('', load_home_page, name='home'),
    path('about/', AboutUsTemplateView.as_view(), name='about'),
    path('general_rules/', GeneralRulesTemplateView.as_view(), name='general rules'),
    path('district/<int:pk>', district, name='district'),
    path('city/<int:pk>', city, name='city'),
    path('area/<int:pk>', area, name='area'),
    path('details/<int:pk>/', show_details, name='show details'),
    path('create_ad/', create_ad, name='create ad'),
    path('approve_ad/<int:pk>/', approve_ad, name='approve ad'),
    path('reject_ad/<int:pk>/', reject_ad, name='reject ad'),
    path('edit_ad/<int:pk>/', edit_ad, name='edit ad'),
    path('delete_ad/<int:pk>/', delete_ad, name='delete ad'),
    path('ajax_load_areas/', load_areas, name='load areas'),
    path('ajax_load_cities/', load_cities, name='load cities'),
    path('rest/', AdListApiView.as_view(), name='ads list api')
]