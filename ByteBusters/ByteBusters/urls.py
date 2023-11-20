"""
URL configuration for ByteBusters project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DentaGraph import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.custom_login, name='custom_login'),
    path('seleccion/', views.seleccion_registro, name='seleccion_registro'),
    #Odontologia
    path('odontologias/', views.odontologia_list, name='odontologia_list'),
    path('odontologias/create/', views.odontologia_create, name='odontologia_create'),
    path('odontologias/update/<int:pk>/', views.odontologia_update, name='odontologia_update'),
    path('odontologias/delete/<int:pk>/', views.odontologia_delete, name='odontologia_delete'),
    #Odontologo
    path('odontologos/', views.odontologo_list, name='odontologo_list'),
    path('odontologos/create/', views.odontologo_create, name='odontologo_create'),
    path('odontologos/update/<int:pk>/', views.odontologo_update, name='odontologo_update'),
    path('odontologos/delete/<int:pk>/', views.odontologo_delete, name='odontologo_delete'),

    #Paciente
    path('pacientes/', views.paciente_list, name='paciente_list'),
    path('pacientes/create/', views.paciente_create, name='paciente_create'),
    path('pacientes/update/<int:pk>/', views.paciente_update, name='paciente_update'),
    path('pacientes/delete/<int:pk>/', views.paciente_delete, name='paciente_delete'),

    #Procedimiento
    path('procedimientos/', views.procedimiento_list, name='procedimiento_list'),
    path('procedimientos/create/', views.procedimiento_create, name='procedimiento_create'),
    path('procedimientos/update/<int:pk>/', views.procedimiento_update, name='procedimiento_update'),
    path('procedimientos/delete/<int:pk>/', views.procedimiento_delete, name='procedimiento_delete'),

    #Estado
    path('estados/', views.estado_list, name='estado_list'),
    path('estados/create/', views.estado_create, name='estado_create'),
    path('estados/update/<int:pk>/', views.estado_update, name='estado_update'),
    path('estados/delete/<int:pk>/', views.estado_delete, name='estado_delete'),

    #Cita
    path('citas/', views.cita_list, name='cita_list'),
    path('citas/create/', views.cita_create, name='cita_create'),
    path('citas/update/<int:pk>/', views.cita_update, name='cita_update'),
    path('citas/delete/<int:pk>/', views.cita_delete, name='cita_delete'),


]
