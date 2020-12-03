from django.shortcuts import render

from estate_app.forms import AdditionalFilterForm


def set_criteria( sale_or_rent, type, number_rooms):
    criteria = {}

    if sale_or_rent != 'Всички':
        criteria['sale_or_rent'] = sale_or_rent
    if type != 'Всички':
        criteria['type'] = type
    if number_rooms != 'Всички':
        criteria['number_rooms'] = number_rooms

    return criteria


def sort_ads(sorting_type, ads):
    if sorting_type == 'Най-нови':
        ads = sorted(ads, key = lambda ad: ad.date_modified, reverse=True)
        return ads
    elif sorting_type == 'Цена Низходяща':
        ads = sorted(ads, key = lambda ad: ad.price, reverse=True)
        return ads
    elif sorting_type == 'Цена Възходяща':
        ads = sorted(ads, key = lambda ad: ad.price, reverse=False)
        return ads
    elif sorting_type == 'Най-гледани':
        ads = sorted(ads, key = lambda ad: ad.counter_seen, reverse=True)
        return ads


def get_ads_filtered_and_sorted(filterinput, ads):
    ads = ads
    sale_or_rent = filterinput.cleaned_data['sale_or_rent']
    type = filterinput.cleaned_data['type']
    number_rooms = filterinput.cleaned_data['number_rooms']
    sort = filterinput.cleaned_data['sort']
    criteria = set_criteria(sale_or_rent, type, number_rooms)
    ads = ads.filter(**criteria)
    if sort == '---':
        return ads
    elif sort == 'Топ оферти':
        ads = [ad for ad in ads if ad.top_offer==True]
    else:
        ads = sort_ads(sorting_type=sort, ads=ads)
    return ads


def process_filter_input(request, context, url, ads, filterinput):
    if filterinput.is_valid():
        ads = get_ads_filtered_and_sorted(filterinput, ads)
        for ad in ads:
            ad.can_modify = request.user.is_superuser or ad.created_by == request.user
        context['ads'] = ads
        if request.user.is_superuser and filterinput.cleaned_data['pending_approval']:
            context['ads'] = [ad for ad in ads if not ad.approved]
            context['pending_approval'] = True

        elif filterinput.cleaned_data['my_add']:
            context['ads'] = [ad for ad in ads if ad.created_by==request.user]
        else:
            context['ads'] = [ad for ad in ads if ad.approved]

        context['filterinput'] = filterinput
        return render(request, url, context)
    else:
        for ad in ads:
            ad.can_modify = request.user.is_superuser or ad.created_by == request.user
        context['ads'] = [ad for ad in ads if ad.approved]
        context['filterinput'] = AdditionalFilterForm()
        return render(request, url, context)

