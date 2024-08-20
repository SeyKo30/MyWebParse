import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.files.base import ContentFile
from .forms import UploadFileForm

API_KEY = "smksergii@gmail.com_SX8G6Lm6ful1HfJRSW3VXbGDtBkTAOXucG2Vak0fMX3Iybdt89VjZR8TuMu6nMe6"
BASE_URL = "https://api.pdf.co/v1"


def convert_doc_to_pdf(file):
    upload_url = upload_file_to_pdfco(file)

    if not upload_url:
        raise Exception("Failed to upload file for conversion.")

    # prepare parameters for conversion
    parameters = {
        "url": upload_url,
        "name": "converted_file.pdf"
    }

    # request to convert the DOC to PDF
    convert_url = f"{BASE_URL}/pdf/convert/from/doc"
    response = requests.post(convert_url, json=parameters, headers={"x-api-key": API_KEY})

    # checking errors
    if response.status_code != 200:
        print(f"Request error: {response.status_code} {response.text}")
        return None

    json_response = response.json()

    if json_response["error"]:
        print(f"Error message: {json_response['message']}")
        return None

    return json_response["url"]


def upload_file_to_pdfco(file):
    upload_url = f"{BASE_URL}/file/upload"

    # Use 'utf-8' encoding to avoid issues with non-ASCII characters
    files = {"file": (file.name.encode('utf-8').decode('latin-1'), file)}

    response = requests.post(upload_url, files=files, headers={"x-api-key": API_KEY})

    if response.status_code != 200:
        print(f"Upload error: {response.status_code} {response.text}")
        return None

    json_response = response.json()

    if json_response["error"]:
        print(f"Upload Error message: {json_response['message']}")
        return None

    return json_response["url"]


def convert_and_download(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            try:
                download_url = convert_doc_to_pdf(uploaded_file)
                if not download_url:
                    return JsonResponse({"error": "Conversion failed."}, status=500)

                # Download the PDF file
                response = requests.get(download_url)
                response.raise_for_status()

                pdf_file = ContentFile(response.content, 'converted_file.pdf')
                response = HttpResponse(pdf_file, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="converted_file.pdf"'

                return response

            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
    else:
        form = UploadFileForm()

    return render(request, 'converter/converter.html', {'form': form})
