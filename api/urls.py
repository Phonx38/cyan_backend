from django.urls import path, include
from .views import analytics
from rest_framework import routers
from api.views import CompanyView

route = routers.DefaultRouter()

route.register("", CompanyView, basename="companyview")

urlpatterns = [
    path("analytics/", analytics),
    path("", include(route.urls)),
]
