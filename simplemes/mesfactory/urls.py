from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'factories', views.FactoryViewSet)
router.register(r'workshops', views.WorkshopViewSet)
router.register(r'lines', views.LineViewSet)
router.register(r'stations', views.StationViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
