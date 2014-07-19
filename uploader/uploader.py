import os
import glob
import logging
import subprocess
import dropbox
from dropbox.client import DropboxClient, ErrorResponse
import settings
from settings import DROPBOX_TOKEN_FILE


def load_dropbox_token():
    with open(DROPBOX_TOKEN_FILE, 'r') as f:
        dropbox_token = f.read()
    return dropbox_token


def has_valid_dropbox_token():
    try:
        with open(DROPBOX_TOKEN_FILE, 'r') as f:
            dropbox_token = f.read()
            client = dropbox.client.DropboxClient(dropbox_token)
            client.account_info()
    except (IOError, ErrorResponse):
        return False
    return True


def get_files_to_upload():
    return glob.glob(settings.IMAGES_DIRECTORY + "/*.jpg")


def upload_file(path):
    access_token = load_dropbox_token()
    client = DropboxClient(access_token)
    name = path.split("/")[-1]
    with open(path, 'rb') as data:
        try:
            client.put_file(name, data)
        except Exception as e:
            logging.exception(e)
        else:
            os.remove(path)


def has_network_connection():
    command = ['ping', '-c', '1', '-W', '2', 'www.dropbox.com']
    try:
        subprocess.check_output(command)
        return True
    except:
        return False
