from PIL import Image


fotografija_izvor = Image.open(r"Fotografije\Algebra_campus.jpg")

# fotografija_izvor.transpose(Image.FLIP_TOP_BOTTOM).show()
# fotografija_izvor.transpose(Image.FLIP_LEFT_RIGHT).show()
# fotografija_izvor.transpose(Image.ROTATE_90).show()
# fotografija_izvor.transpose(Image.ROTATE_180).show()
# fotografija_izvor.transpose(Image.ROTATE_270).show()
# fotografija_izvor.transpose(Image.TRANSPOSE).show()
fotografija_izvor.transpose(Image.TRANSVERSE).show()
