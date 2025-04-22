from PIL import Image, ImageFilter


img = Image.open(r"Fotografije\Algebra_campus.jpg")

# img.filter(ImageFilter.CONTOUR).show()
# img.filter(ImageFilter.EDGE_ENHANCE).show()
# img.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
# img.filter(ImageFilter.EMBOSS).show()
# img.filter(ImageFilter.FIND_EDGES).show()
# img.filter(ImageFilter.SHARPEN).show()
# img.filter(ImageFilter.SMOOTH).show()
# img.filter(ImageFilter.SMOOTH_MORE).show()

# img.filter(ImageFilter.BoxBlur(radius=10)).show()
# img.filter(ImageFilter.GaussianBlur(radius=3)).show()
# img.filter(ImageFilter.UnsharpMask(radius=7, percent=250, threshold=3)).show()
# img.filter(ImageFilter.MaxFilter(size=7)).show()
# img.filter(ImageFilter.MedianFilter(size=7)).show()
img.filter(ImageFilter.MinFilter(size=9)).show()
