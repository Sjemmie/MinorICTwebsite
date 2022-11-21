from PIL import Image

def resize_main(filepath):
    image = Image.open(filepath)
    new_image = image.resize((700,400))
    return new_image

def resize_team(filepath):
    image = Image.open(filepath)
    new_image = image.resize((400,400))
    return new_image

def resize_projecten(filepath):
    image = Image.open(filepath)
    new_image = image.resize((700,400))
    return new_image

def resize_archief(filepath):
    image = Image.open(filepath)
    new_image = image.resize((400,400))
    return new_image