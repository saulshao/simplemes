from django.shortcuts import render

# Create your views here.
from .models import Material, MaterialAttr, Product
from rest_framework import viewsets
from .serializers import MaterialSerializer, ProductSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Material.objects.all().order_by('-updated_on')
    serializer_class = MaterialSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('-updated_on')
    serializer_class = ProductSerializer
