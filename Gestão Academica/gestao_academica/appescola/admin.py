from django.contrib import admin
from .models import Aluno, Professor, Curso, Matricula, Nota

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Matricula)
admin.site.register(Nota)
