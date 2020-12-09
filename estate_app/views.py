from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from estate_app.core.clean_up_images import clean_up_image_files
from estate_app.core.paginator import create_paginator
from estate_app.core.validator import validate_creator
from estate_app.forms import AdditionalFilterForm, AdForm
from estate_app.models import District, DistrictCity, DistrictCityArea, Ad
from estate_app.core.sort_filter import process_filter_input


class AboutUsTemplateView(TemplateView):
    template_name = 'about_us.html'


class GeneralRulesTemplateView(TemplateView):
    template_name = 'general_rules.html'


def load_home_page(request):
    districts = District.objects.all()
    cities = DistrictCity.objects.all()
    areas = DistrictCityArea.objects.all()
    ads = Ad.objects.all()

    context = {
        'districts': districts,
        'cities': cities,
        'areas': areas,
        'ads': ads,
    }
    filterinput = AdditionalFilterForm(request.GET)
    # return process_filter_input(request, context, 'home_page.html', ads, filterinput)
    context = process_filter_input(request, context, ads, filterinput)
    list_ads = context['ads']
    context['page_obj'] = create_paginator(request, list_ads)
    return render(request, 'home_page.html', context)


def district(request, pk):
    selected_district = District.objects.get(pk=pk)
    cities = DistrictCity.objects.filter(district_id=pk)
    areas = DistrictCityArea.objects.all()
    ads = Ad.objects.filter(district=selected_district)
    context = {
        'district': selected_district,
        'cities': cities,
        'areas': areas,
        'ads': ads,
    }
    filterinput = AdditionalFilterForm(request.GET)
    # return process_filter_input(request, context, 'district_page.html', ads, filterinput)
    context = process_filter_input(request, context, ads, filterinput)
    list_ads = context['ads']
    context['page_obj'] = create_paginator(request, list_ads)
    return render(request, 'district_page.html', context)


def city(request, pk):
    selected_city = DistrictCity.objects.get(pk=pk)
    selected_district = District.objects.get(pk=selected_city.district_id)
    areas = DistrictCityArea.objects.filter(city_id=pk)
    ads = Ad.objects.filter(district=selected_district, city=selected_city)
    context = {
        'district': selected_district,
        'city': selected_city,
        'areas': areas,
        'ads': ads,
    }
    filterinput = AdditionalFilterForm(request.GET)
    # return process_filter_input(request, context, 'city_page.html', ads, filterinput)
    context = process_filter_input(request, context, ads, filterinput)
    list_ads = context['ads']
    context['page_obj'] = create_paginator(request, list_ads)
    return render(request, 'city_page.html', context)


def area(request, pk):
    selected_area = DistrictCityArea.objects.get(pk=pk)
    selected_city = DistrictCity.objects.get(pk=selected_area.city_id)
    selected_district = District.objects.get(pk=selected_city.district_id)
    ads = Ad.objects.filter(district=selected_district, city=selected_city, area=selected_area)
    context = {
        'district': selected_district,
        'city': selected_city,
        'area': selected_area,
        'ads': ads,
    }
    filterinput = AdditionalFilterForm(request.GET)
    # return process_filter_input(request, context, 'area_page.html', ads, filterinput)
    context = process_filter_input(request, context, ads, filterinput)
    list_ads = context['ads']
    context['page_obj'] = create_paginator(request, list_ads)
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


def approve_add(request, pk):
    previous_url = request.META.get('HTTP_REFERER')
    ad_to_approve = Ad.objects.get(pk=pk)
    ad_to_approve.approved = True
    ad_to_approve.rejected = False
    ad_to_approve.comments_reject=''
    ad_to_approve.save()
    return redirect(previous_url)


def reject_ad(request, pk):
    previous_url = request.META.get('HTTP_REFERER')
    ad = Ad.objects.get(pk=pk)
    context = {
        'ad_to_reject': AdForm(),
        'ad': ad,
    }
    if request.method == "GET":
        return render(request, 'reject_ad.html', context)
    else:
        comment = request.POST.get('comments_reject')
        ad.rejected = True
        ad.comments_reject = comment
        ad.save()
        return redirect('show details', ad.pk)

@login_required()
def create_add(request):
    previous_url = request.META.get('HTTP_REFERER')
    if request.method == 'GET':
        ad_form = AdForm()
        context = {
            'ad_form': ad_form,
            'previous_url': previous_url
        }
        return render(request, 'create_add_2.html', context)
    else:

        add_form = AdForm(request.POST, request.FILES or None)
        if add_form.is_valid():
            form = add_form.save(commit=False)
            form.created_by = request.user
            form.save()
            return redirect('show details', form.id)
        else:
            context = {
                'ad_form': AdForm(request.POST, request.FILES, instance=add_form)
            }
            return render(request, 'create_add_2.html', context)


@login_required()
def edit_add(request, pk):
    previous_url = request.META.get('HTTP_REFERER')
    ad_to_edit = Ad.objects.get(pk=pk)
    validate_creator(ad_to_edit, request.user)
    if request.method == 'GET':
        context = {
            'ad_form': AdForm(instance=ad_to_edit),
            'reference_number': pk,
            'previous_url': previous_url
        }
        return render(request, 'edit_add.html', context)
    else:
        add_form = AdForm(request.POST, request.FILES or None, instance=ad_to_edit)
        if add_form.is_valid():
            form = add_form.save(commit=False)
            form.date_modified = datetime.now()
            form.approved = False
            form.rejected = False
            form.comments_reject = ''
            form.save()
            return redirect('show details', pk)
        else:
            context = {
                'ad_form': add_form
            }
            return render(request, 'edit_add.html', context)


@login_required()
def delete_add(request, pk):
    ad_to_delete = Ad.objects.get(pk=pk)
    validate_creator(ad_to_delete, request.user)
    clean_up_image_files(ad_to_delete)
    ad_to_delete.delete()
    return redirect('load home')

def load_areas(request):
    city_id = request.GET.get('city_id')
    areas = DistrictCityArea.objects.filter(city_id=city_id).all()
    return render(request, 'area_dropdown_list_options.html', {'areas': areas})


def load_cities(request):
    district_id = request.GET.get('district_id')
    cities = DistrictCity.objects.filter(district_id=district_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
