from django.core.paginator import Paginator

num_items_per_page = 2


def create_paginator(request, list_obj):
    paginator = Paginator(list_obj, num_items_per_page)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj