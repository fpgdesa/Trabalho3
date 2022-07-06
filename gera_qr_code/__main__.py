import qrcode


def gera_qr_code(params):
    
    img = qrcode.make('http://www.uff.br')


    return {'image':img}
