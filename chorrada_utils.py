import os
import random
import sys
import logging
import uuid
import shutil

from logging.handlers import RotatingFileHandler


def get_logger():
    logs_folder_path = os.getenv('LOGS_FOLDER_PATH')
    app_name = os.getenv('APP_NAME')

    if not os.path.isdir(logs_folder_path):
        os.mkdir(logs_folder_path)
    log_file_path = logs_folder_path + '/' + app_name + '.log'
    if not os.path.isfile(log_file_path):
        log_file = open(log_file_path, "a")
        log_file.close()

    logger = logging.getLogger(app_name)
    logger.setLevel('DEBUG')

    log_format = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(log_file_path, maxBytes=(1048576 * 5), backupCount=5)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    logger.info('logger created')

    return logger


# Rename all (jpg, png or gif) images in a folder
def rename_images(logger, folder_path):
    logger.info('renaming images (chorradas)')

    folder_files = os.listdir(folder_path)
    for _, file_name in enumerate(folder_files):
        final_file_name = str(uuid.uuid4())
        original_file_name, extension = os.path.splitext(file_name)
        extension = extension.lower()
        if extension == '.jpg' or extension == '.jpeg' or extension == '.png' or extension == '.gif':
            final_file_path = folder_path + final_file_name + extension
            os.rename(folder_path + file_name, final_file_path)


# Get image
def get_image(logger):
    logger.info('getting image (chorrada)')

    # Get paths
    chorradas_path = os.getenv('IMGS_FOLDER')
    used_path = chorradas_path + '/used/'
    unused_path = chorradas_path + '/unused/'

    # Move image
    # images = os.listdir(unused_path)
    images = [img for img in os.listdir(unused_path) if (img.endswith('.png') or img.endswith('.jpg')) or img.endswith('.gif') or img.endswith('.webp')]
    old_image, extension = os.path.splitext(unused_path + images[0])
    if extension == 'jpeg':
        extension = 'jpg'

    final_image_name = str(uuid.uuid4())
    final_image_path = used_path + final_image_name + extension.lower()
    old_image_path = unused_path + images[0]

    logger.info('old image path: ' + old_image_path)
    logger.info('final image path: ' + final_image_path)
    os.rename(old_image_path, final_image_path)

    # Check image folders
    check_unused_folder(logger, unused_path, used_path)

    return final_image_path


# Check if unused folder is empty
def check_unused_folder(logger, unused_path, used_path):
    logger.info('checking unsused folder')

    unused_images = os.listdir(unused_path)
    used_images = os.listdir(used_path)
    if len(unused_images) == 0:
        for _, image_name in enumerate(used_images):
            shutil.move(used_path + image_name, unused_path)


def create_caption(logger, quotes_file_path):
    logger.info('creating caption')

    quotes = []

    try:
        quotes_file = open(quotes_file_path, 'r')
        quotes_data = quotes_file.readlines()

        for quote in quotes_data:
            quotes.append(quote.strip('\n'))

    except ModuleNotFoundError as error:
        logger.error('something went wrong')
        logger.error(error)

    caption = random.choice(quotes)

    logger.info('caption obtained')

    return caption
