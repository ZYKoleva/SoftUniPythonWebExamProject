from django.shortcuts import render

# Create your views here.
from estate_app.forms import AdditionalFilterForm
from estate_app.models import District, DistrictCity, DistrictCityArea, Ad
from static.others.py_help_func import get_ads_filtered_and_sorted


def about_us(request):
    return render(request, 'about_us.html')


def general_rules(request):
    return render(request, 'general_rules.html')

def load_home_page(request):
    districts = District.objects.all()
    cities = DistrictCity.objects.all()
    areas = DistrictCityArea.objects.all()
    ads = Ad.objects.all()
    for ad in ads:
        ad.is_creator = request.user.is_superuser or ad.created_by_id == request.user.id
    context = {
        'districts': districts,
        'cities': cities,
        'areas': areas,
        'ads': ads,
    }
    filterinput = AdditionalFilterForm(request.GET)
    if filterinput.is_valid():
        ads = get_ads_filtered_and_sorted(filterinput, ads)
        context['ads'] = ads
        context['filterinput'] = filterinput
        return render(request, 'home_page.html', context)
    else:
        context['filterinput'] = AdditionalFilterForm()
    return render(request, 'home_page.html', context)


def district(request, pk):
    selected_district = District.objects.get(pk=pk)
    cities = DistrictCity.objects.filter(district_id=pk)
    areas = DistrictCityArea.objects.all()
    ads = Ad.objects.filter(district=selected_district)
    for ad in ads:
        ad.is_creator = request.user.is_superuser or ad.created_by_id == request.user.id
    context = {
        'district': selected_district,
        'cities': cities,
        'areas': areas,
        'ads': ads,
    }
    filterinput = AdditionalFilterForm(request.GET)
    if filterinput.is_valid():
        ads = get_ads_filtered_and_sorted(filterinput, ads)
        context['ads'] = ads
        context['filterinput'] = filterinput
    else:
        context['filterinput'] = AdditionalFilterForm()
    return render(request, 'district_page.html', context)


def city(request, pk):
    selected_city = DistrictCity.objects.get(pk=pk)
    selected_district = District.objects.get(pk=selected_city.district_id)
    areas = DistrictCityArea.objects.filter(city_id=pk)
    ads = Ad.objects.filter(district=selected_district, city=selected_city)
    for ad in ads:
        ad.is_creator = request.user.is_superuser or ad.created_by_id == request.user.id
    context = {
        'district': selected_district,
        'city': selected_city,
        'areas': areas,
        'ads': ads,
    }
    filterinput = AdditionalFilterForm(request.GET)
    if filterinput.is_valid():
        ads = get_ads_filtered_and_sorted(filterinput, ads)
        context['ads'] = ads
        context['filterinput'] = filterinput
    else:
        context['filterinput'] = AdditionalFilterForm()
    return render(request, 'city_page.html', context)


def area(request, pk):
    selected_area = DistrictCityArea.objects.get(pk=pk)
    selected_city = DistrictCity.objects.get(pk=selected_area.city_id)
    selected_district = District.objects.get(pk=selected_city.district_id)
    ads = Ad.objects.filter(district=selected_district, city=selected_city, area=selected_area)
    for ad in ads:
        ad.is_creator = request.user.is_superuser or ad.created_by_id == request.user.id
    context = {
        'district': selected_district,
        'city': selected_city,
        'area': selected_area,
        'ads': ads,
    }
    filterinput = AdditionalFilterForm(request.GET)
    if filterinput.is_valid():
        ads = get_ads_filtered_and_sorted(filterinput, ads)
        context['ads'] = ads
        context['filterinput'] = filterinput
    else:
        context['filterinput'] = AdditionalFilterForm()
    return render(request, 'area_page.html', context)

def show_details(request, pk):
    ad = Ad.objects.get(pk=pk)
    if request.user.id != ad.created_by_id:
        ad.increase_counter_seen()
        ad.save()
    context = {
        'ad': ad,
    }
    return render(request, 'details.html', context)