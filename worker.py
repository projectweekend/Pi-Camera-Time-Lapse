import glob
from settings import IMAGE
from uploader import DropboxWorker, has_valid_dropbox_token


def main():
    if has_valid_dropbox_token():
        while True:
            files_to_upload = glob.glob(IMAGE.directory + "/*.jpg")
            DropboxWorker(files_to_upload).work()


if __name__ == '__main__':
    main()
