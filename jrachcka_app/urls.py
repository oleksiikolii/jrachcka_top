from django.urls import path
from rest_framework import routers

from jrachcka_app.views import PrinterViewSet, OrderCheckCreate

router = routers.DefaultRouter()

router.register("printers", PrinterViewSet)

urlpatterns = (
    path("bronx/", OrderCheckCreate.as_view()),
)# + router.urls

app_name = "jrachka_app"
