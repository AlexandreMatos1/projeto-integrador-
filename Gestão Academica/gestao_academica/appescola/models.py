from django.db import models

class Aluno(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    nascimento = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    celular = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    acoes = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    aluno_matriculado = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateField()

    def __str__(self):
        return f"{self.aluno_matriculado.nome} - {self.curso.nome}"
    
class Nota(models.Model):
    matricula = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='notas', default=None)
    nota1 = models.CharField(max_length=100)
    nota2 = models.CharField(max_length=100)
    nota3 = models.CharField(max_length=100)

    def __str__(self):
        return f"Nota de {self.matricula.nome}"

