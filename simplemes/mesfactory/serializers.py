from rest_framework import serializers
from models import Factory, FactoryAttr
from models import Workshop, WorkshopAttr
from models import Line, LineAttr
from models import Station, StationAttr


class FactorySerializer(serializers.Serializer):
    class Meta:
        model = Factory
