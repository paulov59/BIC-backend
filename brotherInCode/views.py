from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from .models import *
from .serializers import *

class ContasViewSet(viewsets.ModelViewSet):
    queryset = Contas.objects.all()
    serializer_class = ContasSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]



class TutoresViewSet(viewsets.ModelViewSet):
    queryset = Tutores.objects.all()
    serializer_class = TutoresSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class AreaConhecimentoViewSet(viewsets.ModelViewSet):
    queryset = AreaConhecimento.objects.all()
    serializer_class = AreaConhecimentoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class SubareasConhecimentoViewSet(viewsets.ModelViewSet):
    queryset = SubareasConhecimento.objects.all()
    serializer_class = SubareasConhecimentoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class EspecializacaoTutorViewSet(viewsets.ModelViewSet):
    queryset = EspecializacaoTutor.objects.all()
    serializer_class = EspecializacaoTutorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class InteresseAlunoViewSet(viewsets.ModelViewSet):
    queryset = InteresseAluno.objects.all()
    serializer_class = InteresseAlunoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class HorariosTutorViewSet(viewsets.ModelViewSet):
    queryset = HorariosTutor.objects.all()
    serializer_class = HorariosTutorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class AvaliacaoTutorViewSet(viewsets.ModelViewSet):
    queryset = AvaliacaoTutor.objects.all()
    serializer_class = AvaliacaoTutorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class TutoriaViewSet(viewsets.ModelViewSet):
    queryset = Tutoria.objects.all()
    serializer_class = TutoriaSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    def retrieve(self, request, pk=None):
        try:
            tutoria = Tutoria.objects.get(id=pk)
        except:
            return Response({'error': 'Tutoria não encontrada.'}, status=400)
        return Response(TutoriaSerializer(tutoria).data)
    
    
    @action(detail=False, methods=['get'])
    def minhas_tutorias(self, request, pk=None):
        try:
            aluno = Alunos.objects.get(id_user=request.user)
        except:
            return Response({'error': 'Usuário não é um aluno.'}, status=400)
        tutorias = Tutoria.objects.filter(id_aluno=aluno)
        return Response(TutoriaSerializer(tutorias, many=True).data)