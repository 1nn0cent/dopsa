from PIL import Image, ImageDraw

def make_preview(size, n_colors):
    image = Image.open("image.jpg")
    image.thumbnail(size)
    image = image.quantize(colors = n_colors)
    image.save("res3.bmp", "BMP")
make_preview((400,200), 64)