from rest_framework import routers

from jrachcka_app.views import PrinterViewSet

router = routers.DefaultRouter()

router.register("printers", PrinterViewSet)

urlpatterns = router.urls

app_name = "jrachka_app"