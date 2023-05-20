from django.db import models
from django.contrib.auth.models import User

# VALOR DA TUTORIA É FIXO OU VARIAVEL?

class Contas(models.Model):
    TP_CONTA = (
        ('C', 'Corrente'),
        ('P', 'Poupança'),
    )
    id_conta = models.AutoField(primary_key=True)
    banco = models.CharField(max_length=255)
    agencia = models.CharField(max_length=8)
    conta = models.CharField(max_length=10)
    tipo = models.CharField(max_length=1, choices=TP_CONTA, default='C')
    
    class Meta:
        verbose_name_plural = 'Contas'
        db_table = 'Contas'


class Tutores(models.Model):
    id_tutor = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_conta = models.ForeignKey(Contas, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    
    class Meta:
        verbose_name_plural = 'Tutores'
        db_table = 'Tutores'


class Alunos(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    
    class Meta:
        verbose_name_plural = 'Alunos'
        db_table = 'Alunos'


class AreaConhecimento(models.Model):
    id_area_conhecimento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Áreas do Conhecimento'
        db_table = 'AreaConhecimento'


class SubareasConhecimento(models.Model):
    id_sub_area_conhecimento = models.AutoField(primary_key=True)
    id_area_conhecimento = models.ForeignKey(AreaConhecimento, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Subáreas do Conhecimento'
        db_table = 'SubareasConhecimento'


class EspecializacaoTutor(models.Model):
    id_especializacao_tutor = models.AutoField(primary_key=True)
    id_tutor = models.ForeignKey(Tutores, on_delete=models.CASCADE)
    id_sub_area_conhecimento = models.ForeignKey(SubareasConhecimento, on_delete=models.CASCADE)
    valor = models.FloatField() #vai ser aqui mesmo?
    descricao = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Especializações dos Tutores'
        db_table = 'EspecializacaoTutor'

class ComprovanteEspecializacao(models.Model):
    TP_COMPROVANTE = (
        ('D', 'Diploma'),
        ('C', 'Certificado'),
        ('O', 'Outros')
    )
    id_comprovante_especializacao = models.AutoField(primary_key=True)
    id_especializacao_tutor = models.ForeignKey(EspecializacaoTutor, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TP_COMPROVANTE)
    comprovante = models.FileField(upload_to='comprovantes/especializacao/')

    class Meta:
        verbose_name_plural = 'Comprovantes de Especialização'
        db_table = 'ComprovanteEspecializacao'


class InteresseAluno(models.Model):
    id_interesse_aluno = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    id_sub_area_conhecimento = models.ForeignKey(SubareasConhecimento, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Interesses dos Alunos'
        db_table = 'InteresseAluno'


class HorariosTutor(models.Model):
    id_horario_tutor = models.AutoField(primary_key=True)
    id_tutor = models.ForeignKey(Tutores, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    
    class Meta:
        verbose_name_plural = 'Horários dos Tutores'
        db_table = 'HorariosTutor'


class AvaliacaoTutor(models.Model):
    id_avaliacao_tutor = models.AutoField(primary_key=True)
    id_tutor = models.ForeignKey(Tutores, on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    nota = models.PositiveIntegerField()
    comentario = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Avaliações dos Tutores'
        db_table = 'AvaliacaoTutor'


class Tutoria(models.Model):
    STATUS_TUTORIA = (
        ('A', 'Agendada'),
        ('C', 'Cancelada'),
        ('F', 'Finalizada'),
    )
    
    id_tutoria = models.AutoField(primary_key=True)
    id_tutor = models.ForeignKey(Tutores, on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    id_sub_area_conhecimento = models.ForeignKey(SubareasConhecimento, on_delete=models.CASCADE)
    id_horario_tutor = models.ForeignKey(HorariosTutor, on_delete=models.CASCADE)
    data = models.DateField()
    link = models.URLField()
    status = models.CharField(max_length=1, choices=STATUS_TUTORIA, default='A')
    
    class Meta:
        verbose_name_plural = 'Tutorias'
        db_table = 'Tutoria'
    
class ComprovantePagamento(models.Model):
    id_comprovante_pagamento = models.AutoField(primary_key=True)
    id_tutoria = models.ForeignKey(Tutoria, on_delete=models.CASCADE)
    data = models.DateField()
    comprovante = models.FileField(upload_to='comprovantes/pagamento/')
    
    class Meta:
        verbose_name_plural = 'Comprovantes de Pagamento'
        db_table = 'ComprovantePagamento'
    
