from django.shortcuts import render
from .models import Aluno, Nota
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm
import random

# Create your views here.
def home(request):
    alunos = Aluno.objects.all()
    print(alunos[0])
    return render(request, 'home.html', {'alunos': alunos, 'notas': notas})

def add_aluno(request):
    if request.method == 'POST':
        matricula = gerar_matricula()
        nome = request.POST.get('nome')
        nascimento = request.POST.get('nascimento')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        curso = request.POST.get('curso')
        NovoAluno = Aluno(matricula=matricula, nome=nome, nascimento=nascimento, email=email, celular=celular, curso=curso)
        NovoAluno.save()
        return redirect('home')
    return render(request, 'add_aluno.html')

def gerar_matricula():
    numero_aleatorio = random.randint(10000, 99999)
    matricula = f'M{numero_aleatorio}'
    return matricula

def user_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def editar(request, id):
    aluno = Aluno.objects.get(id=id)
    print(aluno.celular)
    if request.method == 'POST':
        aluno.matricula = request.POST.get('matricula')
        aluno.nome = request.POST.get('nome')
        aluno.nascimento = request.POST.get('nascimento')
        aluno.email = request.POST.get('email')
        aluno.celular = request.POST.get('celular')
        aluno.curso = request.POST.get('curso')
        # EditarAluno = Aluno(matricula=matricula, nome=nome, nascimento=nascimento, email=email, celular=celular, curso=curso)
        aluno.save()
        return redirect('home')
    return render(request, 'editar.html', {'aluno': aluno})

def delete(request,id):

    aluno = Aluno.objects.get(id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('home')
    return render(request, 'delete.html', {'aluno': aluno})

def notas(request, aluno_id):
    aluno = Aluno.objects.get(pk=aluno_id)
    notas = Nota.objects.filter(matricula=aluno)
    return render(request, 'notas.html', {'notas': notas, 'aluno':aluno})

def notas_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    nota = Nota.objects.get(matricula=aluno)
    if request.method == 'POST':
        nota.nota1 = request.POST.get('nota1')
        nota.nota2 = request.POST.get('nota2')
        nota.nota3 = request.POST.get('nota3')
        nota.save()
        return redirect(f'/aluno/{id}/notas/')
    return render(request, 'notas_editar.html', {'nota': nota})