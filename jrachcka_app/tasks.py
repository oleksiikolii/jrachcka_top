import subprocess
import tempfile
import time

from celery import shared_task

from jrachcka_app.models import Check


@shared_task
def add(x, y):
    time.sleep(10)
    print(x + y)
    return x + y


def convert_html_to_pdf(temp_html_file_path):
    pdf_file = temp_html_file_path.replace('.html', '.pdf')
    try:
        subprocess.run(["wkhtmltopdf", temp_html_file_path, pdf_file], check=True)

        return pdf_file
    except subprocess.CalledProcessError as e:
        print(f"Conversion failed. Error: {e}")
        return None


@shared_task
def generate_pdf(check_id, check_html):
    check = Check.objects.filter(id=check_id).first()
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".html") as temp_html_file:
        temp_html_file.write(check_html)
        temp_html_file_path = temp_html_file.name

    pdf_path = convert_html_to_pdf(temp_html_file_path)
    check.pdf_file.save(f"{check_id}_{check.type}.pdf", open(pdf_path, "rb"))
