from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from jrachcka_app.models import Printer, Check
from jrachcka_app.serializers import PrinterSerializer, CheckSerializer
from jrachcka_app.tasks import add


class PrinterViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class OrderCheckCreate(APIView):
    def post(self, request, format=None):
        first_num = request.data.get('first_num')
        second_num = request.data.get('second_num')
        result = add.delay(first_num, second_num)
        print(result)
        return Response({"result": "success"}, status=201)
