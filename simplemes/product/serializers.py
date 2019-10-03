from rest_framework import serializers
from .models import *


class MaterialCategoryAttrSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialCategoryAttr
        fields = ['id', 'attr_name', 'attr_value']


class MaterialCategorySerializer(serializers.HyperlinkedModelSerializer):
    attributes = MaterialCategoryAttrSerializer(many=True)

    class Meta:
        model = MaterialCategory
        fields = ['is', 'url', 'code', 'name', 'description', 'attributes']


class MaterialAttrSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialAttr
        fields = ['id', 'attr_name', 'attr_value']


class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    attributes = MaterialAttrSerializer(many=True)
    material_category = MaterialCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Material
        fields = ['id', 'url', 'code', 'name', 'description', 'material_category', 'attributes']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    master = MaterialSerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ['material_id', 'url', 'master']


class BomTemplateLineSerializer(serializers.ModelSerializer):
    bom_item = MaterialSerializer(many=False, read_only=True)

    class Meta:
        model = BomTemplateLine
        fields = ['id', 'bom_item', 'quantity']


class BomTemplateSerializer(serializers.HyperlinkedModelSerializer):
    bom_lines = BomTemplateLineSerializer(many=True, read_only=False)

    class Meta:
        model = BomTemplate
        fields = ['id', 'url', 'code', 'name', 'description', 'revision', 'bom_lines']
