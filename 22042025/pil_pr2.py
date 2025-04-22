from PIL import Image

fotografija_putanja = r"Fotografije\Algebra_campus.jpg"
fotografija_varijabla = Image.open(fotografija_putanja)


print(f"Dimenzije slike je : \t{fotografija_varijabla.size}.")

x1 = 0 + 500
y1 = 0 + 500
x2 = fotografija_varijabla.size[0] - 500
y2 = fotografija_varijabla.size[1] - 500

print(f"{x1=} {y1=}, {x2=} {y2=}")

fotografija_crop = fotografija_varijabla.crop((x1, y1, x2, y2))

fotografija_crop.save(r"Fotografije\Algebra_campus_crop.jpg", "JPEG")
fotografija_crop.save(r"Fotografije\Algebra_campus_crop.png", "PNG")


fotografija_varijabla.show()
fotografija_crop.show()
