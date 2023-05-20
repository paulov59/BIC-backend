from django.contrib import admin
from django.db.models import Avg

from .models import *

class AvaliacaoTutorInline(admin.TabularInline):
    model = AvaliacaoTutor
    extra = 1
    autocomplete_fields = ['id_aluno']


class ContasForm(admin.ModelAdmin):
    list_display = ['banco', 'agencia', 'conta', 'tipo']
    list_filter = ['banco', 'tipo']
    search_fields = ['banco', 'agencia', 'conta']


class TutoresForm(admin.ModelAdmin):
    def nota(self, obj):
        avaliacoes = AvaliacaoTutor.objects.filter(id_tutor=obj).aggregate(Avg('nota'))
        return avaliacoes['nota__avg']
    
    list_display = ['nome', 'email', 'telefone', 'nota']
    search_fields = ['nome', 'email', 'telefone']
    inlines = [AvaliacaoTutorInline]
    raw_id_fields = ['id_user', 'id_conta']


class AlunosForm(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone']
    search_fields = ['nome', 'email', 'telefone']
    raw_id_fields = ['id_user']


class AreaConhecimentoForm(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


class SubareasConhecimentoForm(admin.ModelAdmin):
    list_display = ['nome', 'id_area_conhecimento']
    search_fields = ['nome']
    list_filter = ['id_area_conhecimento']
    autocomplete_fields = ['id_area_conhecimento']


class EspecializacaoTutorForm(admin.ModelAdmin):
    list_display = ['id_tutor', 'id_sub_area_conhecimento', 'valor']
    search_fields = ['id_tutor']
    list_filter = ['id_sub_area_conhecimento']
    autocomplete_fields = ['id_tutor', 'id_sub_area_conhecimento']


class InteresseAlunoForm(admin.ModelAdmin):
    list_display = ['id_aluno', 'id_sub_area_conhecimento']
    search_fields = ['id_aluno']
    list_filter = ['id_sub_area_conhecimento']
    autocomplete_fields = ['id_aluno', 'id_sub_area_conhecimento']


class HorariosTutorForm(admin.ModelAdmin):
    def tutor(self, obj):
        return obj.id_tutor.nome
    
    list_display = ['tutor', 'dia_semana', 'hora_inicio', 'hora_fim']
    search_fields = ['id_tutor']
    list_filter = ['dia_semana', 'id_tutor']
    autocomplete_fields = ['id_tutor']


class AvaliacaoTutorForm(admin.ModelAdmin):
    def tutor(self, obj):
        return obj.id_tutor.nome
    
    list_display = ['tutor', 'nota', 'comentario']
    search_fields = ['id_tutor']
    list_filter = ['nota']
    autocomplete_fields = ['id_tutor', 'id_aluno']


class TutoriaForm(admin.ModelAdmin):
    def tutor(self, obj):
        return obj.id_tutor.nome

    def aluno(self, obj):
        return obj.id_aluno.nome

    def horario(self, obj):
        return str(obj.id_horario_tutor.hora_inicio) + ' às ' + str(obj.id_horario_tutor.hora_fim)

    list_display = ['tutor', 'aluno', 'data', 'horario', 'status']
    search_fields = ['id_tutor', 'id_aluno']
    list_filter = ['id_tutor', 'data', 'status']
    autocomplete_fields = ['id_tutor', 'id_aluno']
    raw_id_fields = ['id_horario_tutor']
    inlines = [ComprovantePagamentoInline]
admin.site.register(Tutores, TutoresForm)
admin.site.register(Alunos, AlunosForm)
admin.site.register(SubareasConhecimento, SubareasConhecimentoForm)
admin.site.register(EspecializacaoTutor, EspecializacaoTutorForm)
admin.site.register(ComprovanteEspecializacao, ComprovanteEspecializacaoForm)
admin.site.register(HorariosTutor, HorariosTutorForm)
admin.site.register(AvaliacaoTutor, AvaliacaoTutorForm)
admin.site.register(Tutoria, TutoriaForm)
