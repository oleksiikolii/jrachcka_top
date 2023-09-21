from rest_framework import viewsets
from rest_framework.views import APIView

from jrachcka_app.models import Printer, Check
from jrachcka_app.serializers import PrinterSerializer, CheckSerializer


class PrinterViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class OrderCheckCreate(APIView):
    def post(self, request, format=None):
        restaurant_id = request.data.get('restaurant_id')
        printer_type = request.data.get('printer_type')


        order = Check.objects.create()

        try:
            # Перевірка, чи існує принтер типу printer_type для ресторану
            Check.objects.get(order=order, printer_type=printer_type)
            return Response({'message': 'Check already exists for this order and printer type.'}, status=status.HTTP_400_BAD_REQUEST)
        except Check.DoesNotExist:
            Check.objects.create(order=order, printer_type=printer_type)

            # Запуск Celery task для генерації PDF
            generate_pdf.delay(order.id, printer_type)

            return Response({'message': 'Order and check created successfully.'}, status=status.HTTP_201_CREATED)