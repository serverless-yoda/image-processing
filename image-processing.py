import sys
import os
from PIL import Image, ImageFilter

DIR_PATH_DEST_BLUR = './blur-images/'
DIR_PATH_DEST_THUMBNAIL = './thumbnail-images/'
DIR_PATH_DEST_CROP = './cropping-images/'

DIR_PATH_SOURCE = './raw-images/'


def croppingImage(imagepath):
    box = (100, 100, 400, 400)
    with Image.open(f'{DIR_PATH_SOURCE}{imagepath}') as img:
        region = img.crop(box)
        region.save(f'{DIR_PATH_DEST_CROP}{imagepath}')


def thumbnailImage(imagepath):
    size = (128, 128)
    image = Image.open(f'{DIR_PATH_SOURCE}{imagepath}')
    image.thumbnail(size)
    image.save(f'{DIR_PATH_DEST_THUMBNAIL}{imagepath}')


def blurImage(imagepath):
    image = Image.open(f'{DIR_PATH_SOURCE}{imagepath}')
    filter = image.filter(ImageFilter.BLUR)
    filter.save(f'{DIR_PATH_DEST_BLUR}{imagepath}')


def process(path, mode):
    for imagefilename in os.listdir(path):
        mode = mode.lower()
        if mode == 'b':
            blurImage(imagefilename)
        elif mode == 't':
            thumbnailImage(imagefilename)
        elif mode == 'c':
            croppingImage(imagefilename)


if __name__ == '__main__':
    # b = blur
    # t = thumbname
    # c = cropping
    process(DIR_PATH_SOURCE, 'c')
