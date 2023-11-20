from django.shortcuts import render, redirect
from django.urls import get_resolver
from django.contrib import messages
from .models import Odontologia, Odontologo, Paciente, Procedimiento, Estado, Cita
from .forms import OdontologiaForm, OdontologoForm, PacienteForm, ProcedimientoForm, EstadoForm, CitaForm, LoginForm



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

#Paciente

def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'Paciente/paciente_form.html', {'form': form})

def paciente_update(request, pk):
    paciente = Paciente.objects.get(pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'Paciente/paciente_form.html', {'form': form})

def paciente_delete(request, pk):
    Paciente.objects.get(pk=pk).delete()
    return redirect('paciente_list')

#Procedimiento

def procedimiento_create(request):
    if request.method == 'POST':
        form = ProcedimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('procedimiento_list')
    else:
        form = ProcedimientoForm()
    return render(request, 'Procedimiento/procedimiento_form.html', {'form': form})

def procedimiento_update(request, pk):
    procedimiento = Procedimiento.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProcedimientoForm(request.POST, instance=procedimiento)
        if form.is_valid():
            form.save()
            return redirect('procedimiento_list')
    else:
        form = ProcedimientoForm(instance=procedimiento)
    return render(request, 'Procedimiento/procedimiento_form.html', {'form': form})

def procedimiento_delete(request, pk):
    Procedimiento.objects.get(pk=pk).delete()
    return redirect('procedimiento_list')

#Estado

def estado_create(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estado_list')
    else:
        form = EstadoForm()
    return render(request, 'Estado/estado_form.html', {'form': form})

def estado_update(request, pk):
    estado = Estado.objects.get(pk=pk)
    if request.method == 'POST':
        form = EstadoForm(request.POST, instance=estado)
        if form.is_valid():
            form.save()
            return redirect('estado_list')
    else:
        form = EstadoForm(instance=estado)
    return render(request, 'Estado/estado_form.html', {'form': form})

def estado_delete(request, pk):
    Estado.objects.get(pk=pk).delete()
    return redirect('estado_list')


#Cita

def cita_create(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cita_list')
    else:
        form = CitaForm()

    pacientes = Paciente.objects.all()
    odontologos = Odontologo.objects.all()
    procedimientos = Procedimiento.objects.all()
    estados = Estado.objects.all()

    return render(request, 'Cita/cita_form.html', {'form': form, 'pacientes': pacientes, 'odontologos': odontologos, 'procedimientos': procedimientos, 'estados': estados})

def cita_update(request, pk):
    cita = Cita.objects.get(pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('cita_list')
    else:
        form = CitaForm(instance=cita)

    pacientes = Paciente.objects.all()
    odontologos = Odontologo.objects.all()
    procedimientos = Procedimiento.objects.all()
    estados = Estado.objects.all()

    return render(request, 'Cita/cita_form.html', {'form': form, 'pacientes': pacientes, 'odontologos': odontologos, 'procedimientos': procedimientos, 'estados': estados})

def cita_delete(request, pk):
    Cita.objects.get(pk=pk).delete()
    return redirect('cita_list')

#Route /

def list_urls(request):
    urlconf = get_resolver()
    url_list = []
    for url_pattern in urlconf.url_patterns:
        url_list.append(url_pattern.pattern.describe())
    
    return render(request, 'main/list_urls.html', {'url_list': url_list})

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username == 'root' and password == 'root':
            messages.success(request, "Logeo exitoso")
            return redirect('seleccion_registro')
        else:
            messages.error(request, "Usuario no autorizado")
            return redirect('custom_login')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


def seleccion_registro(request):
    return render(request, 'main/seleccion_registro.html')