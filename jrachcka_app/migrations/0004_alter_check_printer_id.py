# Generated by Django 4.2.5 on 2023-09-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jrachcka_app', '0003_remove_restaurant_printers_printer_restaurant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='printer_id',
            field=models.IntegerField(),
        ),
    ]
