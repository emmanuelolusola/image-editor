from PIL import Image, ImageFilter, ImageEnhance
import os

path = "./images"
pathOut = "./editedImages"

for filename in os.listdir(path):
    image = Image.open(f"{path}/{filename}")

    # sharpening, BW
    edit = image.filter(ImageFilter.SHARPEN).convert('L')

    # contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.jpg')

    edit.show()