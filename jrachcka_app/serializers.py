from rest_framework import serializers

from jrachcka_app.models import Printer, Check


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = "__all__"


class CheckSerializer(serializers.ModelSerializer):
    html_content = serializers.CharField(write_only=True)  # Add a field for HTML content

    class Meta:
        model = Check
        fields = '__all__'

    def create(self, validated_data):
        html_content = validated_data.pop('html_content')

        # Create the Check object
        check = Check.objects.create(**validated_data)

        # Call the Celery task to generate the PDF asynchronously
        pdf_task = generate_pdf_from_html.delay(html_content)

        # Save the task ID or any relevant information in the Check model
        check.pdf_generation_task_id = pdf_task.id
        check.save()

        return check
