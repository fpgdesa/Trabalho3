import cv2 
import numpy as np
import urllib
import base64

def main(args):


    nome = 'Fernando' if args.get('nome') is None else args.get('nome')
    sobrenome = 'de Sá' if args.get('sobrenome') is None else args.get('sobrenome')
    endereco = 'Rua Teste, 20' if args.get('end') is None else args.get('end')
    telefone =  '(21) 0000 - 0000' if args.get('telefone') is None else args.get('telefone')
    cidade =   'Rio de Janeiro' if args.get('cidade') is None else args.get('cidade')
    cep =  '20.678-000' if args.get('cep') is None else args.get('cep')
    estado =  'Rio de Janeiro' if args.get('estado') is None else args.get('estado')
    pais = 'Brasil' if args.get('pais') is None else args.get('pais')
    valor = 'R$ 510,00' if args.get('valor') is None else args.get('valor')
    
    url = 'https://raw.githubusercontent.com/fpgdesa/Study/master/boleto.png'
     
    
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    boleto = cv2.imdecode(image, cv2.IMREAD_COLOR)

    
    text_nome = f'{nome} {sobrenome} - contato: {telefone}'
    text_end = f'{endereco} - {cidade}, {estado}, {estado}, {pais}, cep:{cep}'

    position_name = (16,296)
    position_endereco = (16,315)
    position_valor1 = (568,135)
    position_valor2 = (568,264)

    out = cv2.putText(boleto, text_nome, position_name, cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0), 1,cv2.LINE_AA,False)

    out = cv2.putText(out, text_end, position_endereco, cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0), 1,cv2.LINE_AA,False)

    out = cv2.putText(out, valor, position_valor1,cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0), 1,cv2.LINE_AA,False)

    out = cv2.putText(out, valor, position_valor2,cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0), 1,cv2.LINE_AA,False)
    
    cv2.imwrite('temp.png',out)
    
    return {'imagem':str(base64.b64encode(open("temp.png", "rb").read()))}











