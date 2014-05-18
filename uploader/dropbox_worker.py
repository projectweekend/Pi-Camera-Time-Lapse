import os
import logging
from dropbox.client import DropboxClient
from .authentication import load_dropbox_token


class DropboxWorker(object):

    def __init__(self, file_list):
        self.__client = self.__client()
        self.file_list = file_list

    def __client(self):
        access_token = load_dropbox_token()
        return DropboxClient(access_token)

    def __upload_file(self, path):
        file_name = path.split("/")[-1]
        with open(path, 'rb') as file_data:
            try:
                self.client.put_file(file_name, file_data)
            except Exception as e:
                logging.exception(e)
            else:
                self.__clean_up(path)

    def __clean_up(self, path):
        os.remove(path)

    def work(self):
        for path in self.file_list:
            self.__upload_file(path)
