from django.shortcuts import render
from base.forms import ContatoForm, ReservaBanhoForm
from base.models import Contato, ReservaBanho

def inicio(request):
    return render(request, 'inicio.html')

def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'telefone': '(92) 98239-0513',
        'responsavel': 'Bruno Almeida',
        'form': form,
        'sucesso': sucesso
    }
    return render(request,'contato.html', contexto)

def reservabanho(request):
    sucesso = False
    form = ReservaBanhoForm(request.POST or None)
    if form.is_valid():
            sucesso = True
            form.save()
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
        
    return render(request,'reservabanho.html', contexto)