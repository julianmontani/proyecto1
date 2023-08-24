from django.urls import path
from MiApp.views import * #CursoListView, eliminar_curso, registrar_curso, docente, curso

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registrarCurso/', registrar_curso),
    path('eliminacionCurso/<int:id>/', eliminar_curso, name='eliminar_curso'),
    path('Docente/', docente, name='docente'),
    path('cursos/', lista_cursos, name='cursos'),
    path('crear-curso/', cursos, name='crear-cursos'),
    path('Directivos/', directivos, name='directivos'),
    path('inicio', inicio),
    path('cursos/', cursos, name='cursos'),
    path('busquedaComision/', busquedaComision, name='busquedaComision'),
    path('buscar/', buscar, name='buscar'),
]