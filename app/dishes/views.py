from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from app.dishes.serializer import CategorySerializer, DishSerializer
from app.dishes.models import Category, Dish


@api_view(['GET', 'POST'])
@permission_classes((AllowAny, ))
def dish_list(request):
    if request.method == 'GET':
        response_data = {}
        dish = Dish.objects.all()
        dish_serializer = DishSerializer(dish, many=True)
        return Response(
            {
                'code':
                200,
                'message':
                'Verification email has been sent to your email. Please verify your account.',
                'data':
                dish_serializer.data
            },
            status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        dish_name = data.get("name")
        category_id = data.get("category_id")
        profile_id = 1
        mrp = data.get("mrp")
        offer_price = data.get("offer_price")
        is_veg = data.get("is_veg")
        time_slot = data.get("time_slot", [])
        dish, created = Dish.objects.get_or_create(
            name=dish_name,
            category_id=category_id,
            profile_id=profile_id,
            mrp=mrp,
            offer_price=offer_price,
            is_veg=is_veg,
            time_slot=time_slot)
        dish_serializer = DishSerializer(dish, many=False)
        return Response(
            {
                'code': 201 if created else 200,
                'message': 'Category created successfully',
                'data': dish_serializer.data
            },
            status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def categories(request):
    if request.method == 'GET':
        response_data = {}
        data = request.query_params
        show_products = data.get("products", 0)
        selectedCategory = data.get("selectedCategory", None)
        category = Category.objects.filter(
            id=selectedCategory) if selectedCategory else Category.objects.all(
            )
        response_data["categories"] = CategorySerializer(
            category,
            many=True,
            context={
                'list_dishes': True if show_products else False
            }).data
        return Response(
            {
                'code': 200,
                'message': 'Category list fetched successfully',
                'data': response_data
            },
            status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        category_name = data.get("name", None)

        category, created = Category.objects.get_or_created(name=category_name)
        category_serializer = CategorySerializer(category, many=False)
        return Response(
            {
                'code': 201 if created else 200,
                'message': 'Category created successfully',
                'data': category_serializer.data
            },
            status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes((AllowAny, ))
def dish_quantity(request):
    data = request.data
    dish_id = data.get("dish_id")
    quantity = data.get("quantity", 0)
    print data
    try:
        dish = Dish.objects.get(id=dish_id)
        dish.quantity = quantity
        dish.save()
    except Dish.DoesNotExist:
        return Response(
            {
                'code': 400,
                'message': 'Menu item not found',
                'data': None
            },
            status=status.HTTP_404_NOT_FOUND)
    dish_serializer = DishSerializer(dish, many=False)
    return Response(
        {
            'code': 200,
            'message': 'Quantity updated successfully',
            'data': dish_serializer.data
        },
        status=status.HTTP_200_OK)
