from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Materia, Docente, Directivo, Curso 
from .forms import CursoForm, DocenteForm

def home(request):
    cursosListados = Curso.objects.all().order_by('nombre')
    data = {
        'titulo': 'Gestion de Cursos',
        'cursos': cursosListados
    }
    return render(request, 'gestionCursos.html', data)

class CursoListView(ListView):
    model = Curso
    template_name = 'gestionCursos.html'

    def get_queryset(self):
        return Curso.objects.all()
    

def registrar_curso(request):
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso=Curso.objects.create(nombre=nombre, creditos=creditos)
    return render(request, 'materias.html')


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('/')

def cursos(request):
    if request.method=='POST':
        form=CursoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            creditos=info['creditos']
            curso=Curso(nombre=nombre,creditos=creditos)
            curso.save()
            return render(request, 'cursos.html', {'mensaje':'Curso Creado'})
        return render(request, 'cursos.html', {'mensaje':'Datos Invalidos'})
    else:
        formulario_curso=CursoForm
        return render(request, 'cursos.html', {'formulario': formulario_curso})
    

def directivos(request):
    directivos = Directivo.objects.all()
    return render(request, 'directivo.html', {'directivos': directivos})

def docente(request):
    if request.method=='POST':
        form=DocenteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            apellido_paterno=info['apellido paterno']
            apellido_materno=info['apellido materno']
            nombres=info['nombre']
            fechas_nacimiento=['edad']
            sexos=['genero']
            docente=Docente(nombres=nombres,apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, fechas_nacimiento=fechas_nacimiento, sexos=sexos)
            docente.save()
            formulario_docente=DocenteForm()
            return render(request, 'docente.html', {'mensaje':'Docente Creado', 'formulario':formulario_docente})
        else:
            return render(request, 'docente.html', {'mensaje':'Datos Invalidos'})
    else:

        formulario_docente=DocenteForm()

    return render(request,'docente.html', {'formulario':formulario_docente})

def lista_cursos(request):
    cursos=Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def inicio(request):
    return render(request, 'inicio.html')

def busquedaComision(request):
    return render(request, 'busquedaComision.html')

def buscar(request):
    nombre=request.GET['nombre']
    if nombre!='':
        cursos=Curso.objects.filter(nombre__icontains=nombre)
        return render(request, 'resultadosBusqueda.html', {'cursos':cursos})
    else:
        return render(request, 'busquedaComision.html', {'mensaje':'no me ha ingresado nada'})

def materias(request):
    cursos=Curso.objects.all()
    return render(request, 'materias.html', {'cursos': cursos})
    
    
