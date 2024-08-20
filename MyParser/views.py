from django.shortcuts import render
from .forms import UploadFileForm
from .parsers.pdf_parser import parse_pdf
import os


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            # временный путь для сохранения загруженного файла
            file_path = f'/tmp/{uploaded_file.name}'

            # проверка правильного расширения
            if not file_path.endswith(".pdf"):
                return render(request, 'MyParser/upload_result.html',
                              {'filename': uploaded_file.name,
                               'content': "Unsupported file type. Only PDF files are allowed."},
                              status=400)

            # Сохраняем загруженный PDF-файл на сервере
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            try:
                # Парсим PDF-файл
                text = parse_pdf(file_path)
            except Exception as e:
                # на случай ошибки парсинга
                return render(request, 'MyParser/upload_result.html',
                              {'filename': uploaded_file.name, 'content': f"Error parsing file: {str(e)}"},
                              status=500)
            finally:
                 #удаляем загруженный файл после обработки
                if os.path.exists(file_path):
                    os.remove(file_path)

            # Отправляем результат в шаблон
            return render(request, 'MyParser/upload_result.html', {
                'filename': uploaded_file.name,
                'content': text,
                'file_url': request.build_absolute_uri(f'/filtered-content/?filename={uploaded_file.name}')
            })

    else:
        form = UploadFileForm()

    # Отправляем форму для загрузки файла
    return render(request, 'MyParser/upload.html', {'form': form})

