from django.db import models


class CheckType(models.TextChoices):
    KITCHEN = "kitchen"
    CLIENT = "client"


class Printer(models.Model):
    name = models.CharField(max_length=127)
    api_key = models.CharField(max_length=255, unique=True)
    check_type = models.CharField(max_length=127, choices=CheckType.choices)
    restaurant = models.ForeignKey(to="Restaurant", related_name="printers", on_delete=models.CASCADE)

    def __str__(self):
        return f"Printer num {self.id}, {self.name}, {self.check_type}"


class Check(models.Model):
    class StatusType(models.TextChoices):
        NEW = "new"
        RENDERED = "rendered"
        PRINTED = "printed"

    printer_id = models.IntegerField()
    type = models.CharField(max_length=127, choices=CheckType.choices)
    order = models.JSONField()
    status = models.CharField(max_length=127, choices=StatusType.choices)
    pdf_file = models.FileField(null=True)


class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}, {self.printers}"