from django import forms
from .models import Paciente

class PacienteModelForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'dnasc', 'email', 'typeteste', 'resteste']