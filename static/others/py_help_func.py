def set_criteria(sale_or_rent, type, number_rooms):
    criteria = {}
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