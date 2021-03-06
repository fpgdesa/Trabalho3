# Trabalho 3

 - O trabalho consiste na implementação da arquitetura serverless para gerar duas formas de pagamento: Boleto e PIX (aqui representado pela geração de um simples QR Code).
 
 - Dois serviços atuam para a realização dessas tarefas

 - Um terceiro serviço gera o elemento div do módulo de pagamento
 
 - Os serviços foram implementados utilizando o framework da Apache Openwhisk



# Ativação:

    - Building docker container: docker-compose build web
    - Run container on port 8000: docker-compose up -d

# Visão Geral:

![alt text](https://raw.githubusercontent.com/fpgdesa/Trabalho3/main/pagina.png)


## Serviço 1 - elemento div
    - A ação será invocada para gerar o elemento html responsável por exibir informações do produto comprado.
    - Criação da ação: wsk action create div_pagamento div_pagamento.py --web True 
    - Invocação da ação: wsk action invoke --result div_pagamento
    - Invocação da ação (url): https://us-east.functions.cloud.ibm.com/api/v1/web/uff_pagamento/default/div_pagamento

![alt text](https://raw.githubusercontent.com/fpgdesa/Trabalho3/main/modulo_paga.png)

## Serviço 2 - geração do QR code
    - A ação é invocada para a geração de um QR code contendo um link de direcionamento
    - Esta ação utiliza bibliotecas externas (pyqrcode e pypng)
    - Um ambiente virtual foi gerado e comprimido em arquivo *.zip para a geração da ação
    - Criação da ação: wsk action update qr_code qr_code.zip --kind python:3 --web True
    - Invocação da ação: wsk action invoke qr_code -r
    - Invocação da ação (url): https://us-east.functions.cloud.ibm.com/api/v1/web/uff_pagamento/default/qr_code

## Serviço 3 - geração do boleto bancário
    - A ação é invocada para a geração de um boleto bancário contendo informações do usuário no ato da compra de um computador
    - Esta ação utiliza bibliotecas externas de processamento de imagens (OpenCV) e processamento de dados (NumPy)
    - Como o ambiente virtual gerado ultrapassa o limite de armazenamento do OpenWhisk, uma imagem docker foi gerada
    - O arquivo Dockerfile contém as instruções da imagem gerada utilizando como base a imagem 'openwhisk/python3action:latest'
    - Após a realização do build na imagem, ela é enviada para o dockerhub
    - Criação da ação: wsk action create gera_boleto __main__.py --docker fpgdesa/python3action:boleto_docker
    - Invocação da ação: wsk action invoke gera_boleto -r
    - Invocação da ação (url): https://us-east.functions.cloud.ibm.com/api/v1/web/uff_pagamento/default/gera_boleto
    - O dicionário fornecido pela ação contém a imagem do boleto gerado codificado utilizando a biblioteca Base64






