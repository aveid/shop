from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name', 'parent',
        ]

    def to_representation(self, instance):
        representaion = super().to_representation(instance)
        if instance.cat.exists:
            representaion['cat'] = CategorySerializer(
                instance.cat.all(), many=True).data
        return representaion