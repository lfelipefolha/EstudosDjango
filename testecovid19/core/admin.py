from django.contrib import admin

from .models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email', 'dnasc', 'typeteste', 'resteste','criado', 'modificado', 'ativo')