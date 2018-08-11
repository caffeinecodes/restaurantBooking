from app.dishes.models import Category, Dish
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField('products_fun')

    def products_fun(self, instance):
        dish_serializer = []
        if 'list_dishes' in self.context and self.context['list_dishes']:
            dishes = Dish.objects.filter(category=instance)
            dish_serializer = DishSerializer(dishes, many=True).data
        return dish_serializer

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug_name', 'products')


class DishSerializer(serializers.ModelSerializer):
    time_slots = serializers.SerializerMethodField('time_slots_func')

    @staticmethod
    def time_slots_func(instance):
        print instance.time_slot
        return eval(instance.time_slot)

    class Meta:
        model = Dish
        fields = ('id', 'name', 'slug_name', 'thumbnail', 'is_veg',
                  'description', 'time_slots', 'mrp', 'offer_price',
                  'quantity')
