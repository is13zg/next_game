from PIL import Image
from PIL import ImageDraw
import random

w = 500
h = 500
pc = 80

while True:
    im1 = Image.new('RGB', (w, h), 'white')  # background image
    с = 0
    x = 0
    while с < w * h * pc / 100:
        x += 1
        wi = random.randint(0, w - 2)
        hi = random.randint(0, h - 2)
        pix = im1.load()
        if pix[wi, hi] == (255, 255, 255) and pix[wi + 1, hi] == (255, 255, 255) and pix[wi, hi + 1] == (
                255, 255, 255) and \
                pix[wi + 1, hi + 1] == (255, 255, 255):
            pix[wi, hi] = (0, 0, 0)
            pix[wi + 1, hi] = (0, 0, 0)
            pix[wi, hi + 1] = (0, 0, 0)
            pix[wi + 1, hi + 1] = (0, 0, 0)
            с += 4
        if x == 1000000:
            break

    im1.save(f"{pc}pcfill.jpg")
    if True:
        break
