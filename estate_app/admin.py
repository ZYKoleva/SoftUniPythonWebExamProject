from django.contrib import admin

# Register your models here.
from estate_app.models import District, DistrictCity, DistrictCityArea, Ad, AdditionalFilter,TypePremise, \
    SaleOrRent, NumberRooms, Construction, Elevator, Furniture, SortOptions


class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'area', 'type_premise', 'created_by', 'approved', 'rejected')
    list_filter = ('approved', 'date_modified', 'rejected')


admin.site.register(District)
admin.site.register(Ad, AdAdmin)
admin.site.register(DistrictCity)
admin.site.register(DistrictCityArea)
admin.site.register(TypePremise)
admin.site.register(SaleOrRent)
admin.site.register(NumberRooms)
admin.site.register(Construction)
admin.site.register(Elevator)
admin.site.register(Furniture)
admin.site.register(AdditionalFilter)
admin.site.register(SortOptions)

