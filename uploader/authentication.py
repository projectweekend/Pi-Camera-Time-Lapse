import dropbox
from dropbox.client import ErrorResponse
from .settings import DROPBOX_TOKEN_FILE


def has_valid_dropbox_token():
    try:
        with open(DROPBOX_TOKEN_FILE, 'r') as f:
            dropbox_token = f.read()
            client = dropbox.client.DropboxClient(dropbox_token)
            client.account_info()
    except (IOError, ErrorResponse):
        return False
    return True


def display_token_instructions():
    print('MISSING DROPBOX TOKEN!')
    print('1. Go to https://rpi-camera-uploader.herokuapp.com/ and click "Get started"')
    print('2. "Allow" Raspberry Pi Camera Uploader access to Dropbox')
    print('3. Put downloaded "dropbox.txt" in root of "/Pi-Camera-Time-Lapse"')
