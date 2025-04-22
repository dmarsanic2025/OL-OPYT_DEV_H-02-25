from PIL import Image, ImageDraw


img = Image.open(r"Fotografije\Algebra_campus.jpg")

img_draw = ImageDraw.Draw(img)
img_draw.rectangle((800, 500, 3400, 2200), fill=None, outline="red", width=15)
# img.show()

img_draw.ellipse((800, 500, 3400, 2200), fill=None, outline="blue", width=15)
img.show()
