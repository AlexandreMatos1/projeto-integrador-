# Generated by Django 5.0.1 on 2024-03-21 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appescola', '0005_rename_aluno_matriculado_nota_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
