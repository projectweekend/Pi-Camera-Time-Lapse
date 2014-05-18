import yaml
import utils


with open('settings.yml') as settings_file:
    YML = yaml.safe_load(settings_file)
    IMAGE = utils.Settings(YML['image'])
    SNAP = utils.Settings(YML['snap'])

DROPBOX_TOKEN_FILE = "./dropbox.txt"
