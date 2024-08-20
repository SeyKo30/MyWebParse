# myparser/utils.py

import requests


def convert_docx_to_pdf(docx_path, pdf_path):
    api_key = '077c107c500e2ad39e6a324e76e7f7ccdc721909'
    endpoint = 'https://api.zamzar.com/v1/jobs'

    # Шаг 1: Создание задания на конвертацию
    files = {
        'source_file': open(docx_path, 'rb')
    }
    data = {
        'target_format': 'pdf'
    }
    response = requests.post(endpoint, files=files, data=data, auth=(api_key, ''))

    if response.status_code != 201:
        raise Exception('Failed to create conversion job: ' + response.text)

    # Получение ID задания
    job_id = response.json()['id']

    # Шаг 2: Проверка состояния задания и ожидание завершения
    while True:
        status_response = requests.get(f'{endpoint}/{job_id}', auth=(api_key, ''))
        status = status_response.json()['status']

        if status == 'successful':
            # скачивание результат
            result_file_url = status_response.json()['target_files'][0]['url']
            result_response = requests.get(result_file_url)
            with open(pdf_path, 'wb') as pdf_file:
                pdf_file.write(result_response.content)
            break
        elif status == 'failed':
            raise Exception('Conversion job failed: ' + status_response.text)
