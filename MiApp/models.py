from django.db import models
from django.utils.html import format_html

from .choices import sexos

# Create your models here.

class Docente(models.Model):
    apellido_paterno=models.CharField(max_length=20, verbose_name='Apellido_paterno')
    apellido_materno=models.CharField(max_length=20, verbose_name='Apellido_materno')
    nombres=models.CharField(max_length=20, verbose_name='nombres')
    fecha_nacimiento=models.DateField(verbose_name='Fecha de Nacimiento')
    sexo=models.CharField(max_length=1, choices=sexos, default='F')

    def nombre_completo(self):
        return '{} {}, {}'.format(self.apellido_paterno,self.apellido_materno,self.nombres)
    
    def __str__(self):
        return self.nombre_completo()
    
    class Meta:
        verbose_name='Docente'
        verbose_name_plural='Docentes'
        db_table='docente'
        ordering=['apellido_paterno', '-apellido_materno']

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente=models.ForeignKey(Docente,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Directivo(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente=models.ForeignKey(Docente,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre