from django.shortcuts import render
from app.dishes.models import Dish
from django.http import Http404, HttpResponse
from app.dishes.serializer import CategorySerializer, DishSerializer


def index(request):
    return render(request, 'admin/index.html')


def item_list(request):
    return render(request, 'admin/item-list.html')


def add_menu(request):
    return render(request, 'admin/add-menu.html')


def item_details(request, slug_name):
    context = {}
    try:
        dish = Dish.objects.get(slug_name=slug_name)
        context['dish'] = DishSerializer(dish, many=False).data
    except Dish.DoesNotExist:
        raise Http404()
    return render(request, 'admin/item-details.html', context)


def edit_menu(request):
    return render(request, 'admin/edit-menu.html')