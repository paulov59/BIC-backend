# Generated by Django 4.2.1 on 2023-05-27 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brotherInCode', '0004_alter_alunos_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacaotutor',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
    ]
