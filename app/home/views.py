from django.shortcuts import render


def index(request):
    return render(request, 'admin/index.html')


def item_list(request):
    return render(request, 'admin/item-list.html')


def add_menu(request):
    return render(request, 'admin/add-menu.html')


def item_details(request):
    return render(request, 'admin/item-details.html')


def edit_menu(request):
    return render(request, 'admin/edit-menu.html')