from django.contrib import admin

from jrachcka_app.models import Restaurant, Check, Printer


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    pass


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    pass
