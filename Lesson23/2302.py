from PIL import Image

def calculate_average_rgb(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        total_r, total_g, total_b = 0, 0, 0
        
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))
                total_r += r
                total_g += g
                total_b += b
        
        num_pixels = width * height
        average_r = total_r // num_pixels
        average_g = total_g // num_pixels
        average_b = total_b // num_pixels
        
        return average_r, average_g, average_b

def main():
    image_path = 'image.jpg'
    average_r, average_g, average_b = calculate_average_rgb(image_path)
    print(average_r, average_g, average_b)

if __name__ == '__main__':
    main()
