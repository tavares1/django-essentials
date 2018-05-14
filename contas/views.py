from django.shortcuts import render, redirect
from .models import Transacao
from .forms import TransacaoForm
import datetime


def home(request):
    data = {}
    data["transacoes"] = Transacao.objects.all()
    return render(request, 'contas/home.html', data)


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'contas/form.html', {'form': form})


def update(request, pk):
    data = {}
    # Recebendo valor de PK
    transacao = Transacao.objects.get(pk=pk)
    # Ou recebe um metodo post ou a instancia de uma transação que vai ser modificada.
    form = TransacaoForm(request.POST or None, instance=transacao)
    # Pode utilizar a mesma validação e o mesmo template do metodo de CREATE.
    if form.is_valid():
        form.save()
        return redirect('home')
    data['form'] = form
    print(form.fields)
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    data = {}
    # Receber o object a ser deletado do banco
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('home')