from rest_framework import routers

from .views import *

routerBrotherInCode = routers.DefaultRouter()
routerBrotherInCode.register(r'contas', ContasViewSet)
routerBrotherInCode.register(r'tutores', TutoresViewSet)
routerBrotherInCode.register(r'alunos', AlunosViewSet)
routerBrotherInCode.register(r'areaconhecimento', AreaConhecimentoViewSet)
routerBrotherInCode.register(r'subareasconhecimento', SubareasConhecimentoViewSet)
routerBrotherInCode.register(r'especializacaotutor', EspecializacaoTutorViewSet)
routerBrotherInCode.register(r'interessealuno', InteresseAlunoViewSet)
routerBrotherInCode.register(r'horariostutor', HorariosTutorViewSet)
routerBrotherInCode.register(r'avaliacaotutor', AvaliacaoTutorViewSet)
routerBrotherInCode.register(r'tutoria', TutoriaViewSet)