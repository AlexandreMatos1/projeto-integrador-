# Generated by Django 5.0.1 on 2024-03-06 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appescola', '0002_aluno_acoes_aluno_celular_aluno_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.CharField(max_length=100)),
                ('nota1', models.CharField(max_length=100)),
                ('nota2', models.CharField(max_length=100)),
                ('nota3', models.CharField(max_length=100)),
            ],
        ),
    ]
