from django.shortcuts import render

# Create your views here.
from estate_app.forms import AdditionalFilterForm
from estate_app.models import District, DistrictCity, DistrictCityArea, Ad
from static.others.py_help_func import set_criteria, sort_ads, get_ads_filtered_and_sorted


def about_us(request):
    return render(request, 'about_us.html')


def general_rules(request):
    return render(request, 'general_rules.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def load_home_page(request):
    districts = District.objects.all()
    cities = DistrictCity.objects.all()
    areas = DistrictCityArea.objects.all()
    ads = Ad.objects.all()
    if request.method == "GET":
        context = {
            'districts': districts,
            'cities': cities,
            'areas': areas,
            'ads': ads,
            'filterinput': AdditionalFilterForm()
        }
        return render(request, 'home_page.html', context)
    else:
        filterinput = AdditionalFilterForm(request.POST)
        if filterinput.is_valid():
            ads = get_ads_filtered_and_sorted(filterinput, ads)
            context = {
                'districts': districts,
                'cities': cities,
                'areas': areas,
                'filterinput': filterinput,
                'ads': ads,
            }
            return render(request, 'home_page.html', context)


def district(request, pk):
    selected_district = District.objects.get(pk=pk)
    cities = DistrictCity.objects.filter(district_id=pk)
    areas = DistrictCityArea.objects.all()
    ads = Ad.objects.filter(district=selected_district)
    if request.method == "GET":
        context = {
            'district': selected_district,
            'cities': cities,
            'areas': areas,
            'ads': ads,
            'filterinput': AdditionalFilterForm()
        }
        return render(request, 'district_page.html', context)
    else:
        filterinput = AdditionalFilterForm(request.POST)
        if filterinput.is_valid():
            sale_or_rent = filterinput.cleaned_data['sale_or_rent']
            type = filterinput.cleaned_data['type']
            number_rooms = filterinput.cleaned_data['number_rooms']
            sort = filterinput.cleaned_data['sort']
            criteria = set_criteria(sale_or_rent, type, number_rooms)
            ads = ads.filter(**criteria)
            sorted_ads = sort_ads(sorting_type=sort, ads=ads)
            context = {
                'district': selected_district,
                'cities': cities,
                'areas': areas,
                'filterinput': filterinput,
                'ads': sorted_ads,
            }
            return render(request, 'district_page.html', context)


def city(request, pk):
    selected_city = DistrictCity.objects.get(pk=pk)
    selected_district = District.objects.get(pk=selected_city.district_id)
    areas = DistrictCityArea.objects.filter(city_id=pk)
    ads = Ad.objects.filter(district=selected_district, city=selected_city)
    if request.method == "GET":
        context = {
            'district': selected_district,
            'city': selected_city,
            'areas': areas,
            'ads': ads,
            'filterinput': AdditionalFilterForm()
        }
        return render(request, 'city_page.html', context)
    else:
        filterinput = AdditionalFilterForm(request.POST)
        if filterinput.is_valid():
            sale_or_rent = filterinput.cleaned_data['sale_or_rent']
            type = filterinput.cleaned_data['type']
            number_rooms = filterinput.cleaned_data['number_rooms']
            sort = filterinput.cleaned_data['sort']
            criteria = set_criteria(sale_or_rent, type, number_rooms)
            ads = ads.filter(**criteria)
            sorted_ads = sort_ads(sorting_type=sort, ads=ads)
            context = {
                'district': selected_district,
                'city': selected_city,
                'areas': areas,
                'filterinput': filterinput,
                'ads': sorted_ads,
            }
            return render(request, 'city_page.html', context)


def area(request, pk):
    selected_area = DistrictCityArea.objects.get(pk=pk)
    selected_city = DistrictCity.objects.get(pk=selected_area.city_id)
    selected_district = District.objects.get(pk=selected_city.district_id)
    ads = Ad.objects.filter(district=selected_district, city=selected_city, area=selected_area)
    if request.method == "GET":
        context = {
            'district': selected_district,
            'city': selected_city,
            'area': selected_area,
            'ads': ads,
            'filterinput': AdditionalFilterForm()
        }
        return render(request, 'area_page.html', context)
    else:
        filterinput = AdditionalFilterForm(request.POST)
        if filterinput.is_valid():
            sale_or_rent = filterinput.cleaned_data['sale_or_rent']
            type = filterinput.cleaned_data['type']
            number_rooms = filterinput.cleaned_data['number_rooms']
            sort = filterinput.cleaned_data['sort']
            criteria = set_criteria(sale_or_rent, type, number_rooms)
            ads = ads.filter(**criteria)
            sorted_ads = sort_ads(sorting_type=sort, ads=ads)
            context = {
                'district': selected_district,
                'city': selected_city,
                'area': selected_area,
                'filterinput': filterinput,
                'ads': sorted_ads,
            }
            return render(request, 'area_page.html', context)