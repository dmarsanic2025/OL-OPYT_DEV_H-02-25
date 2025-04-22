from PIL import Image, ImageEnhance


img = Image.open(r"Fotografije\Algebra_campus.jpg")


img_e1 = ImageEnhance.Brightness(img)
# img_e1.enhance(4).show()

img_e2 = ImageEnhance.Contrast(img)
# img_e2.enhance(4).show()

img_e3 = ImageEnhance.Sharpness(img)
# img_e3.enhance(4).show()


img_e4 = ImageEnhance.Color(img)
img_e4.enhance(4).show()
