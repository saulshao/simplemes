from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from .models import Factory, Workshop, Line, Station
from .models import FactoryAttr, WorkshopAttr, LineAttr, StationAttr
from rest_framework import viewsets
from .serializers import FactorySerializer


class FactoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows factories to be viewed or edited.
    """
    queryset = Factory.objects.all().order_by('-updated_on')
    serializer_class = FactorySerializer
