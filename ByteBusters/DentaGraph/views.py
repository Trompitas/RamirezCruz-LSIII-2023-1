from django.shortcuts import render, redirect
from django.urls import get_resolver
from .models import Odontologia, Odontologo, Paciente, Procedimiento, Estado, Cita
from .forms import OdontologiaForm, OdontologoForm, PacienteForm, ProcedimientoForm, EstadoForm, CitaForm


def odontologia_list(request):
    odontologias = Odontologia.objects.all()
    return render(request, 'Odontologia/odontologia_list.html', {'odontologias': odontologias})

def odontologo_list(request):
    odontologos = Odontologo.objects.all()
    return render(request, 'Odontologo/odontologo_list.html', {'odontologos': odontologos})

def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'Paciente/paciente_list.html', {'pacientes': pacientes})

def procedimiento_list(request):
    procedimientos = Procedimiento.objects.all()
    return render(request, 'Procedimiento/procedimiento_list.html', {'procedimientos': procedimientos})

def estado_list(request):
    estados = Estado.objects.all()
    return render(request, 'Estado/estado_list.html', {'estados': estados})

def cita_list(request):
    citas = Cita.objects.all()
    return render(request, 'Cita/cita_list.html', {'citas': citas})

#Odontologia

def odontologia_create(request):
    if request.method == 'POST':
        form = OdontologiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('odontologia_list')
    else:
        form = OdontologiaForm()
    return render(request, 'Odontologia/odontologia_form.html', {'form': form})

def odontologia_update(request, pk):
    odontologia = Odontologia.objects.get(pk=pk)
    if request.method == 'POST':
        form = OdontologiaForm(request.POST, instance=odontologia)
        if form.is_valid():
            form.save()
            return redirect('odontologia_list')
    else:
        form = OdontologiaForm(instance=odontologia)
    return render(request, 'Odontologia/odontologia_form.html', {'form': form})

def odontologia_delete(request, pk):
    Odontologia.objects.get(pk=pk).delete()
    return redirect('odontologia_list')

#Odontologo

def odontologo_create(request):
    if request.method == 'POST':
        form = OdontologoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('odontologo_list')
    else:
        form = OdontologoForm()
    return render(request, 'Odontologo/odontologo_form.html', {'form': form})

def odontologo_update(request, pk):
    odontologo = Odontologo.objects.get(pk=pk)
    if request.method == 'POST':
        form = OdontologoForm(request.POST, instance=odontologo)
        if form.is_valid():
            form.save()
            return redirect('odontologo_list')
    else:
        form = OdontologoForm(instance=odontologo)
    return render(request, 'Odontologo/odontologo_form.html', {'form': form})

def odontologo_delete(request, pk):
    Odontologo.objects.get(pk=pk).delete()
    return redirect('odontologo_list')


#Route /

def list_urls(request):
    urlconf = get_resolver()
    url_list = []
    for url_pattern in urlconf.url_patterns:
        url_list.append(url_pattern.pattern.describe())
    
    return render(request, 'main/list_urls.html', {'url_list': url_list})
