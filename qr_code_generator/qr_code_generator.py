import pyqrcode
link = input("Link : ")
url = pyqrcode.create(link)
url.svg("myqr.svg", scale = 8)
url.png('myqr.png', scale = 6)
