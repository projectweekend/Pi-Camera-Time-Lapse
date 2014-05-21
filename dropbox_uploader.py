#!/usr/bin/env python

import os
import glob
import logging
from dropbox.client import DropboxClient
from uploader import load_dropbox_token, has_valid_dropbox_token
import settings


access_token = load_dropbox_token()


def main():
    if has_valid_dropbox_token():
        client = DropboxClient(access_token)
        paths = glob.glob(settings.IMAGES_DIRECTORY + "/*.jpg")
        for path in paths:
            name = path.split("/")[-1]
            with open(path, 'rb') as data:
                try:
                    client.put_file(name, data)
                except Exception as e:
                    logging.exception(e)
            os.remove(path)


if __name__ == '__main__':
    while True:
        main()
