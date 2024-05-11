# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
import os

current_dir = os.path.dirname(__file__)
filename = os.path.join(current_dir, r"myqr.png")

# String which represents the QR code
s = "https://forms.gle/an4BXskNZUNnQctQ7"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.png(filename, scale = 6)
