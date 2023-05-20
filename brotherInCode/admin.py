from django.contrib import admin

from .models import *

admin.site.register(Contas)
admin.site.register(Tutores)
admin.site.register(Alunos)
admin.site.register(AreaConhecimento)
admin.site.register(SubareasConhecimento)
admin.site.register(EspecializacaoTutor)
admin.site.register(InteresseAluno)
admin.site.register(HorariosTutor)
admin.site.register(AvaliacaoTutor)
admin.site.register(Tutoria)