from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from .models import Factory, Workshop, Line, Station
from rest_framework import viewsets
from .serializers import FactorySerializer, WorkshopSerializer, LineSerializer, StationSerializer


class FactoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows factories to be viewed or edited.
    """
    queryset = Factory.objects.all().order_by('-updated_on')
    serializer_class = FactorySerializer


class WorkshopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows factories to be viewed or edited.
    """
    queryset = Workshop.objects.all().order_by('-updated_on')
    serializer_class = WorkshopSerializer


class LineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows factories to be viewed or edited.
    """
    queryset = Line.objects.all().order_by('-updated_on')
    serializer_class = LineSerializer


class StationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows factories to be viewed or edited.
    """
    queryset = Station.objects.all().order_by('-updated_on')
    serializer_class = StationSerializer
