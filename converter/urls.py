from django.urls import path
from .views import convert_and_download

app_name = 'converter'

urlpatterns = [
    path('convert/', convert_and_download, name='convert'),
]
