from PIL import Image

def resize(filepath):
    image = Image.open(filepath)
    new_image = image.resize((400,400))
    return new_image