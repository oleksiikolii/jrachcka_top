# import os
# from celery import shared_task
# from django.conf import settings
# from django.template.loader import render_to_string
# from weasyprint import HTML
#
# from jrachcka_app.models import Check
#
#
# @shared_task
# def generate_pdf(order_id, printer_type):
#     order = Check.objects.get(pk=order_id)
#     html_content = render_to_string('order_template.html', {'order': order})
#
#     # Generate PDF
#     pdf_data = HTML(string=html_content).write_pdf()
#
#     # Save PDF
#     pdf_filename = f"{order_id}_{printer_type}.pdf"
#     pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdf', pdf_filename)
#     with open(pdf_path, 'wb') as pdf_file:
#         pdf_file.write(pdf_data)
#
#     # Mark Check as generated
#     check = Check.objects.get(order=order, printer_type=printer_type)
#     check.generated = True
#     check.save()

from celery import shared_task

@shared_task
def add(x, y):
    return x + y

