from django import forms
from .models import Odontologia, Odontologo, Paciente, Procedimiento, Estado, Cita
from django.contrib.auth.forms import AuthenticationForm


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configura el queryset para los campos
        self.fields['paciente'].queryset = Paciente.objects.all()
        self.fields['odontologo'].queryset = Odontologo.objects.all()
        self.fields['procedimiento'].queryset = Procedimiento.objects.all()
        self.fields['estado'].queryset = Estado.objects.all()



class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
