from PIL import Image

fotografija_putanja = r"Fotografije\Algebra_campus.jpg"
fotografija_varijabla = Image.open(fotografija_putanja)

fotografija_varijabla_convert = fotografija_varijabla.convert(mode="L")

fotografija_varijabla_convert.show()
