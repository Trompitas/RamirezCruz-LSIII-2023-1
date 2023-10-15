from django.db import models

class Odontologia(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

class Odontologo(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)

class Procedimiento(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=8, decimal_places=2)

class Estado(models.Model):
    estado = models.CharField(max_length=50)

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    odontologo = models.ForeignKey(Odontologo, on_delete=models.CASCADE)
    procedimiento = models.ForeignKey(Procedimiento, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

class Meta:
    db_table = 'odontologias',
    db_table = 'odontologos',
    db_table = 'pacientes',
    db_table = 'procedimientos',
    db_table = 'estados',
    db_table = 'citas'
