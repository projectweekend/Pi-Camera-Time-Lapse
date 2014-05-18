import glob
from settings import IMAGE
from uploader import DropboxWorker


def get_file_list():
    return glob.glob(IMAGE.directory + "/*.jpg")


if __name__ == '__main__':
    files_to_upload = get_file_list()
    DropboxWorker(files_to_upload).work()
