from PIL import Image

def twist_image(output_file_name):
    input_file_name = 'statement-image.jpg' 
    image = Image.open(input_file_name)
    width, height = image.size
    left_half = (0, 0, width // 2, height)
    right_half = (width // 2, 0, width, height)
    left_image = image.crop(left_half)
    right_image = image.crop(right_half)
    new_image = Image.new('RGB', (width, height))
    new_image.paste(right_image, (0, 0))
    new_image.paste(left_image, (width // 2, 0))
    new_image.save(output_file_name, 'JPEG')

twist_image('output-image.jpg')
