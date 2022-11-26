import os

import cv2
import matplotlib.pyplot as plt
from PIL import Image

from Clustering import segment_image

DATA_PATH = '/home/lqnk/PycharmProjects/PlantsTF/input/Plant_leave_diseases_dataset_with_augmentation'


def print_sample_images():
    for plantClassFolder in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, plantClassFolder)
        for img in os.listdir(path):
            image = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)
            plt.imshow(image)
            plt.title(f'{plantClassFolder}')
            plt.show()
            break


def rgb_plot(image_path):
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")  # 3D plot with scalar values in each axis

    im = Image.open(image_path)
    r, g, b = list(im.getdata(0)), list(im.getdata(1)), list(im.getdata(2))

    axis.scatter(r, g, b, c="#ff0000", marker="o")
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")
    plt.show()


def main():
    exit(0)


if __name__ == '__main__':
    main()
