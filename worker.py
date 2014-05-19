import glob
from settings import IMAGE
from uploader import DropboxWorker


if __name__ == '__main__':
    while True:
        files_to_upload = glob.glob(IMAGE.directory + "/*.jpg")
        DropboxWorker(files_to_upload).work()
