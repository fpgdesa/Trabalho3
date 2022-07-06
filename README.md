# Trabalho 3


 - O trabalho consiste na implementação da arquitetura serverless para gerar duas formas de pagamento: Boleto e PIX (aqui representado pela geração de um simples QR Code).
 
 - Dois serviços atuam para a realização dessas tarefas

 - Um terceiro serviço gera o elemento div do módulo de pagamento
 
 - Os serviços foram implementados utilizando o framework da Apache Openwhisk




# Visão Geral:

![alt text](https://raw.githubusercontent.com/fpgdesa/Trabalho3/main/pagina.png)


## Serviço 1 - elemento div
    - A ação será invocada para gerar o elemento html responsável por exibir informações do produto comprado.
    - Criação da ação: wsk action create div_pagamento div_pagamento.py --web True 
    - Invocação da ação: wsk action invoke --result div_pagamento
    - Invocação da ação (url): https://us-east.functions.cloud.ibm.com/api/v1/web/uff_pagamento/default/div_pagamento

![alt text](https://raw.githubusercontent.com/fpgdesa/Trabalho3/main/modulo_paga.png)




