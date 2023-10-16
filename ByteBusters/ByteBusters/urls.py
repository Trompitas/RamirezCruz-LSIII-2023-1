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
    path('', views.list_urls, name='list_urls'),
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
]
