#Import Library
import qrcode
img=qrcode.make('www.google.com')
img.save('Hello.jpg')
