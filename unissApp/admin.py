from django.contrib import admin

from unissApp.models import *

class ProfesoresAdmin(admin.ModelAdmin):
    list_display = ('telefono','ci','nombre','fecha')
    search_fields  = ('telefono','ci','nombre')
    list_filter  = ('telefono','ci','nombre','fecha')


admin.site.register(Profesor,ProfesoresAdmin)
admin.site.register(Clase)
admin.site.register(Estudiante)
