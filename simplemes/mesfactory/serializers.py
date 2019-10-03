from rest_framework import serializers
from .models import Factory, FactoryAttr
from .models import Workshop, WorkshopAttr
from .models import Line, LineAttr
from .models import Station, StationAttr


class StationAttrSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationAttr
        fields = ['id', 'attr_name', 'attr_value']


class StationSerializer(serializers.HyperlinkedModelSerializer):
    attributes = StationAttrSerializer(many=True)

    class Meta:
        model = Station
        fields = ['id', 'url', 'code', 'name', 'description', 'attributes']


class LineAttrSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineAttr
        fields = ['id', 'attr_name', 'attr_value']


class LineSerializer(serializers.HyperlinkedModelSerializer):
    attributes = LineAttrSerializer(many=True)
    stations = StationSerializer(many=True, read_only=True)

    class Meta:
        model = Line
        fields = ['id', 'url', 'code', 'name', 'description', 'attributes', 'stations']


class WorkshopAttrSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkshopAttr
        fields = ['id', 'attr_name', 'attr_value']


class WorkshopSerializer(serializers.HyperlinkedModelSerializer):
    attributes = WorkshopAttrSerializer(many=True)
    lines = LineSerializer(many=True, read_only=True)

    class Meta:
        model = Workshop
        fields = ['id', 'url', 'code', 'name', 'description', 'attributes', 'lines']


class FactoryAttrSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryAttr
        fields = ['id', 'attr_name', 'attr_value']


class FactorySerializer(serializers.HyperlinkedModelSerializer):
    attributes = FactoryAttrSerializer(many=True)
    workshops = WorkshopSerializer(many=True, read_only=True)

    class Meta:
        model = Factory
        fields = ['id', 'url', 'code', 'name', 'description', 'attributes', 'workshops']
