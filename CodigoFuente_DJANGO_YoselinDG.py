# PowerShell: Crear entorno virtual y activarlo
PS C:\Users\silva> python -m venv yoss
(yoss) PS C:\Users\silva> yoss\Scripts\activate

# Instalar Django y virtualenv
(yoss) PS C:\Users\silva> pip install django
(yoss) PS C:\Users\silva> python.exe -m pip install virtualenv

# Verificar versión de Django
(yoss) PS C:\Users\silva> django-admin --version

# Crear proyecto y aplicación Django, y ejecutar el servidor
(yoss) PS C:\Users\silva> django-admin startproject myproject
(yoss) PS C:\Users\silva> cd myproject
(yoss) PS C:\Users\silva\myproject> python manage.py startapp polls
(yoss) PS C:\Users\silva\myproject> cd ..
(yoss) PS C:\Users\silva> code myproject
(yoss) PS C:\Users\silva\myproject> python manage.py runserver



# Archivo views.py en la aplicación pollsapp
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the pollsapp index. -YoselinDG")



# Archivo urls.py en la aplicación pollsapp
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]


# Archivo urls.py en el proyecto myproject
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('pollsapps.urls')),
    path('admin/', admin.site.urls),
]
