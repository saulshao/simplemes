from django.shortcuts import render

# Create your views here.
from .models import MaterialCategory, Material, Product, BomTemplate
from rest_framework import viewsets
from .serializers import MaterialSerializer, ProductSerializer, MaterialCategorySerializer, BomTemplateSerializer


class MaterialCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MaterialCategory.objects.all().order_by('-updated_on')
    serializer_class = MaterialCategorySerializer


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


class BomTemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = BomTemplate.objects.all().order_by('-updated_on')
    serializer_class = BomTemplateSerializer
