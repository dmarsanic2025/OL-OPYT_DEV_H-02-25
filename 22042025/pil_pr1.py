from PIL import Image

fotografija_putanja = r"Fotografije\Algebra_campus.jpg"

fotografija_varijabla = Image.open(fotografija_putanja)

print()
print(fotografija_varijabla)
print(f"Format slike je : \t{fotografija_varijabla.format}.")
print(f"Mod slike je : \t{fotografija_varijabla.mode}.")
print(f"Dimenzije slike je : \t{fotografija_varijabla.size}.")

fotografija_varijabla.show()
