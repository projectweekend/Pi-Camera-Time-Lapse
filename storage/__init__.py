DROPBOX_KEY_FILE = "./dropbox.txt"


def load_dropbox_key():
    try:
        with open(DROPBOX_KEY_FILE, 'r') as f:
            output = f.read()
    except IOError:
        output = ""
    return output


def save_dropbox_key(dropbox_key):
    with open(DROPBOX_KEY_FILE, 'w+') as f:
        f.write(dropbox_key)
    return dropbox_key


