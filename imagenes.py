from PIL import Image
import os


# This program changes all the PNG images on a folder to the size of your choice
# And adds a white background to the image instead of the transparent background

def resize(image_pil, width, height):
    '''
    Resize PIL image keeping ratio and using white background.
    '''
    ratio_w = width / image_pil.width
    ratio_h = height / image_pil.height
    if ratio_w < ratio_h:
        # It must be fixed by width
        resize_width = width
        resize_height = round(ratio_w * image_pil.height)
    else:
        # Fixed by height
        resize_width = round(ratio_h * image_pil.width)
        resize_height = height
    image_resize = image_pil.resize((resize_width, resize_height), Image.ANTIALIAS)
    background = Image.new('RGBA', (width, height), (255, 255, 255, 255))
    offset = (round((width - resize_width) / 2), round((height - resize_height) / 2))
    background.paste(image_resize, offset)
    return background.convert('RGB')


def resize_white(img, basewidth):
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    image = img
    new_image = Image.new("RGBA", image.size, "WHITE")  # Create a white rgba background
    new_image.paste(image, (0, 0), image)  # Paste the image on the background.
    new_image.convert('RGB')
    return resize(new_image, 1500, 1500)


# Substitute InputFolder
images = [file for file in os.listdir('InputFolder') if file.endswith(('jpeg', 'png', 'jpg'))]
for image in images:
    imagen = Image.open('InputFolder//' + image)
    if image.endswith(('jpeg', 'jpg')):
        resize(imagen, 1500, 1500).save('OutputFolder//' + image, "JPEG")  # Substitute OutputFolder
    else:
        resize_white(imagen, 1500).save("OutputFolder//" + image, "JPEG")  # Substitute OutputFolder
