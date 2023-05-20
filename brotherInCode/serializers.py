from rest_framework import serializers

from .models import *

class ContasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contas
        fields = '__all__'

class TutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutores
        fields = '__all__'

class AlunosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alunos
        fields = '__all__'

class AreaConhecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaConhecimento
        fields = '__all__'

class SubareasConhecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubareasConhecimento
        fields = '__all__'

class EspecializacaoTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspecializacaoTutor
        fields = '__all__'

class InteresseAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteresseAluno
        fields = '__all__'

class HorariosTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorariosTutor
        fields = '__all__'

class AvaliacaoTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaoTutor
        fields = '__all__'

class TutoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutoria
        fields = '__all__'
    
    def to_representation(self, obj):
        try:
            tutor = {
                'id_tutor': obj.id_tutor.pk,
                'nome': obj.id_tutor.nome,
            }
        except:
            tutor = None
        
        try:
            horario = {
                'id_horario': obj.id_horario.pk,
                'dia': obj.id_horario.dia_semana,
                'hora_inicio': obj.id_horario.hora_inicio,
                'hora_fim': obj.id_horario.hora_fim,
            }
        except:
            horario = None
        
        return {
            'id_tutoria': obj.id_tutoria,
            'tutor': tutor,
            'data': obj.data,
            'horario': horario,
            'subarea_conhecimento': obj.id_sub_area_conhecimento.nome,
            'link': obj.link,
            'status': obj.status,
        }