from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CoreApplication.urls', namespace='CoreApplication')),
    path('parser/', include('MyParser.urls', namespace='MyParser')),
    path('converter/', include('converter.urls', namespace='converter')),
]