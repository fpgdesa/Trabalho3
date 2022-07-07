import pyqrcode
import png
from pyqrcode import QRCode
import base64

def main(params):
    
    img = pyqrcode.create('http://www.uff.br')
    
    img.png('myqr.png', scale = 6)


    return {'image':str(base64.b64encode(open("myqr.png", "rb").read()))}
