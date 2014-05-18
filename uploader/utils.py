import dropbox
from .settings import DROPBOX_TOKEN_FILE


def has_valid_dropbox_token():
    try:
        with open(DROPBOX_TOKEN_FILE, 'r') as f:
            dropbox_token = f.read()
            client = dropbox.client.DropboxClient(dropbox_token)
            client.account_info()
    except (IOError, dropbox.client.ErrorResponse):
        return False
    return True


def load_dropbox_key():
    try:
        with open(DROPBOX_TOKEN_FILE, 'r') as f:
            output = f.read()
    except IOError:
        output = ""
    return output


def save_dropbox_key(dropbox_key):
    with open(DROPBOX_TOKEN_FILE, 'w+') as f:
        f.write(dropbox_key)
    return dropbox_key
