import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = input("Bir link yaz : ")

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "mysqr.svg"
url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.svg"
url.png('myqr.png', scale = 8)
