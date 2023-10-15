from django import forms
from .models import Odontologia, Odontologo, Paciente, Procedimiento, Estado, Cita

class OdontologiaForm(forms.ModelForm):
    class Meta:
        model = Odontologia
        fields = '__all__'

class OdontologoForm(forms.ModelForm):
    class Meta:
        model = Odontologo
        fields = '__all__'

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class ProcedimientoForm(forms.ModelForm):
    class Meta:
        model = Procedimiento
        fields = '__all__'

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = '__all__'

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'
