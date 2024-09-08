from PIL import Image, ImageFilter

def motion_blur(n):
    image = Image.open('image.jpg')
    rotated_image = image.rotate(270)
    blurred_image = rotated_image.filter(ImageFilter.GaussianBlur(radius=n))
    blurred_image.save('res.jpg')


motion_blur(5)
