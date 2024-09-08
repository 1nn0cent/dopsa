from PIL import Image
 
 
def transparency(filename1, filename2):
    img1 = Image.open(filename1)
    img2 = Image.open(filename2)
    first_pixs = img1.load()
    second_pixs = img2.load()
    w, h = img1.size
    for x in range(w):
        for y in range(h):
            r1, g1, b1 = first_pixs[x, y]
            r2, g2, b2 = second_pixs[x, y]
            new_pixs = (int(0.5 * r1 + 0.5 * r2),
                        int(0.5 * g1 + 0.5 * g2),
                        int(0.5 * b1 + 0.5 * b2))
            first_pixs[x, y] = new_pixs
    img1.save("trans.jpg")
transparency('fish.jpg','space.jpg')