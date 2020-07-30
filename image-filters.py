# Inspired in https://www.instagram.com/p/CDDV7gxgK_c/

from PIL import Image, ImageFilter

im1 = Image.open(r"img.png")

im2 = im1.filter(ImageFilter.BLUR)
im3 = im1.filter(ImageFilter.CONTOUR)
im4 = im1.filter(ImageFilter.EMBOSS)
im5 = im1.filter(ImageFilter.EDGE_ENHANCE)

im1.show()
im2.show()
im3.show()
im4.show()
im5.show()
