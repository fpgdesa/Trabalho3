from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.views.decorators.csrf import csrf_protect

Infos = {'metodo':'Boleto',
         'nome': '',
         'sobrenome':'',
         'end':'',
         'telefone':'',
         'cidade':'',
         'cep':'',
         'valor':'R$ 510,00',
         'estado':'Rio de Janeiro',
         'pais':'Brasil'}

class StartPage(View):
    def get(self,request):
        return render(request,"index.html")
        

@csrf_exempt
def gerar_pagamento(request):

    Infos['nome'] = request.POST.get('nome')
    Infos['sobrenome'] = request.POST.get('sobrenome')
    Infos['end'] = request.POST.get('end')
    Infos['telefone'] = request.POST.get('telefone')
    Infos['cidade'] = request.POST.get('cidade')
    Infos['cep'] = request.POST.get('cep')

    print(Infos)
  
    

    return HttpResponse("")



@csrf_exempt
def metodo_pagamento(request):
    Infos['metodo'] = request.POST.get('progress')
    print(Infos)
    return HttpResponse("")

@csrf_exempt
def nome(request):
    Infos['nome'] = request.POST.get('progress')
    print(Infos)
    return HttpResponse("")
