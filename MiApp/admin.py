from django.contrib import admin
from .models import Curso, Docente, Directivo

# Register your models here.


class Cursoadmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creditos')
    search_fields = ('nombre', 'creditos')
    list_display_links = ('nombre',)


admin.site.register(Curso, Cursoadmin)


admin.site.register(Docente)

admin.site.register(Directivo)