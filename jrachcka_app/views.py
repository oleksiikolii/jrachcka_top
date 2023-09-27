import json

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from jrachcka_app.models import Printer, Check, Restaurant
from jrachcka_app.serializers import PrinterSerializer, CheckSerializer
from jrachcka_app.tasks import add, generate_pdf


class PrinterViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class OrderCheckCreate(APIView):
    def post(self, request):
        order_data = json.loads(request.body)
        order_no = order_data.get("order_no")
        restaurant = Restaurant.objects.filter(id=order_data.get("restaurant_id")).first()
        print(restaurant.printers.all())
        products = order_data.get("products")

        printer_kitchen = restaurant.printers.filter(check_type="kitchen").first()

        kitchen_check = Check.objects.create(
            printer_id=printer_kitchen.id,
            type="kitchen",
            order=json.dumps(products),
            status="new",
        )

        context = {
            "data": products,
            "order_no": order_no
        }
        kitchen_check_html = render(
            request,
            "order_template.html",
            context=context
        ).content.decode("utf-8")

        generate_pdf.delay(kitchen_check.id, kitchen_check_html)

        return Response({"order_created": "success"}, status=201)
