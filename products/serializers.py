from rest_framework import serializers
from .models import Products
from category.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Products
        fields = ['name', 'description', 'image', 'price', 'category',]