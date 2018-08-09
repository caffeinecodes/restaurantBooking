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


@api_view(['GET'])
@permission_classes((AllowAny, ))
def dish_list(request):
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


@api_view(['GET'])
@permission_classes((AllowAny, ))
def categories(request):
    if request.method == 'GET':
        category = Category.objects.all()
        category_serializer = CategorySerializer(category, many=True)
        return Response(
            {
                'code': 200,
                'message': 'Category list fetched successfully',
                'data': category_serializer.data
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
