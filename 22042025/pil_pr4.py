from PIL import Image


fotografija_izvor = Image.open(r"Fotografije\Algebra_campus.jpg")
fotografija_wm = Image.open(r"Fotografije\Python_logo_and_wordmark.png")

print(fotografija_izvor.size)
print(fotografija_wm.size)

fotografija_izvor.paste(fotografija_wm, (500, 300))

fotografija_izvor.show()

fotografija_izvor.close()
