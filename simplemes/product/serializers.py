from rest_framework import serializers
from .models import Material, Product


class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = ['code', 'name', 'description', 'material_category']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['material.code', 'material.name', 'material.description']
