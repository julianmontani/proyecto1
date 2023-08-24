from django import forms
from .models import Docente, Curso, Directivo, Materia
from .choices import sexos

class DocenteForm(forms.Form):
    apellido_paterno=forms.CharField(max_length=20)
    apellido_materno=forms.CharField(max_length=20)
    nombres=forms.CharField(max_length=20)
    fecha_nacimiento=forms.DateField()
    sexo=forms.ChoiceField()

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    creditos = forms.IntegerField()

class DirectivoForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=50)


class MateriaForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    creditos = forms.IntegerField()
    




