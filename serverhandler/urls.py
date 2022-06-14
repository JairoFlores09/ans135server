from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ues/', include('metodos.urls')),
    path('admin/', admin.site.urls),
]
