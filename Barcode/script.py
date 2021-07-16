from barcode import EAN13
from barcode.writer import ImageWriter

# Write to an image
with open('barcode.jpeg', 'wb') as f:
    EAN13('100000011111', writer=ImageWriter()).write(f)