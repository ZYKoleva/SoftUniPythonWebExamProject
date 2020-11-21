from django.contrib import admin

# Register your models here.
from estate_app.models import District, DistrictCity, DistrictCityArea, Ad, AdditionalFilter

admin.site.register(District)
admin.site.register(DistrictCity)
admin.site.register(DistrictCityArea)
admin.site.register(Ad)
admin.site.register(AdditionalFilter)

