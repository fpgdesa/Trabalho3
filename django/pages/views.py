from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.views.decorators.csrf import csrf_protect
import os
import pycurl
from io import BytesIO 

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

        b_obj = BytesIO() 
        crl = pycurl.Curl() 

        # Set URL value
        crl.setopt(crl.URL, 'https://us-east.functions.cloud.ibm.com/api/v1/web/uff_pagamento/default/div_pagamento.json')

        # Write bytes that are utf-8 encoded
        crl.setopt(crl.WRITEDATA, b_obj)

        # Perform a file transfer 
        crl.perform() 

        # End curl session
        crl.close()

# Get the content stored in the BytesIO object (in byte characters) 
        get_body = b_obj.getvalue()

        output = get_body.decode('utf8')

        output = output.replace("\\n","").replace("\\","").replace("\n","")[17:-2]








        return render(request,"index.html",  context={'div_pagamento': output})
        

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
    
    
def get_div_pagamento(request):
    #print(os.system('wsk action invoke --result div_pagamento'))
    return render(request,"index.html", 
    		   context={ 'div_pagamento':1000}
    		)
 
 
 
