from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'materialcategories', views.MaterialCategoryViewSet)
router.register(r'materials', views.MaterialViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'bomtemplates', views.BomTemplateViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
