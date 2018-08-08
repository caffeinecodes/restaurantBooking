from app.dishes.models import Category, Dish
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug_name')


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'slug_name', 'thumbnail', 'is_veg',
                  'description', 'time_slot', 'mrp', 'offer_price')
