from PIL import Image
import os


def scale_image(image_path):
    im = Image.open(image_path)
    image = im.convert('RGB')
    file_name = os.path.basename(image_path)
    image.thumbnail((224, 224))
    image.save(image_path, 'JPEG')


def scale_data(data_path):
    for plantClassFolder in os.listdir(data_path):
        path = os.path.join(data_path, plantClassFolder)
        for img in os.listdir(path):
            scale_image(os.path.join(path, img))


class ImageScalerFunctions:
    pass
