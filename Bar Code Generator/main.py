import barcode
from barcode.writer import ImageWriter

br = barcode.get_barcode_class('code39')
BR = br('debjit9674003240', writer=ImageWriter())
br_code = BR.save('barcode')