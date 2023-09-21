from django.db import models


class CheckType(models.TextChoices):
    KITCHEN = "kitchen"
    CLIENT = "client"


class Printer(models.Model):
    name = models.CharField(max_length=127)
    api_key = models.CharField(max_length=255, unique=True)
    check_type = models.CharField(max_length=127, choices=CheckType.choices)


class Check(models.Model):
    class StatusType(models.TextChoices):
        NEW = "new"
        RENDERED = "rendered"
        PRINTED = "printed"

    printer_id = models.ForeignKey(to=Printer, on_delete=models.CASCADE)
    type = models.CharField(max_length=127, choices=CheckType.choices)
    order = models.JSONField()
    status = models.CharField(max_length=127, choices=StatusType.choices)
    pdf_file = models.FileField()
