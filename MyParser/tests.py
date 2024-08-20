from django.test import TestCase
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .parsers.pdf_parser import parse_pdf
import os


class PDFParserTests(TestCase):

    def create_test_pdf(self):
        """Создает простой PDF-файл в памяти с текстом 'Hello World'."""
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        c.drawString(100, 750, "Hello World")
        c.showPage()
        c.save()
        buffer.seek(0)
        return buffer

    def test_parse_pdf(self):
        """Проверяет, что функция parse_pdf правильно извлекает текст из PDF."""
        # Создаем тестовый PDF-файл в памяти
        pdf_buffer = self.create_test_pdf()
        temp_file_path = '/tmp/test.pdf'

        # Сохраняем в файл
        with open(temp_file_path, 'wb') as temp_file:
            temp_file.write(pdf_buffer.read())

        # Вызов функции для извлечения текста из PDF
        extracted_text = parse_pdf(temp_file_path)

        # Проверяем, что извлеченный текст соответствует ожидаемому
        self.assertIn("Hello World", extracted_text)

        # Очистка: удаляем временный файл
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
