import glob
import yaml
import utils


with open('settings.yml') as settings_file:
    YML = yaml.safe_load(settings_file)
    IMAGE = utils.Settings(YML['image'])
    SNAP = utils.Settings(YML['snap'])

DROPBOX_TOKEN_FILE = "./dropbox.txt"
WORKING_DIRECTORY = "/home/pi/time-lapse"
IMAGES_DIRECTORY = WORKING_DIRECTORY + "/images"
JOBS_DIRECTORY = WORKING_DIRECTORY + "/jobs"


class Setting(object):

    def __init__(self, settings_dict):
        self.__dict__.update(settings_dict)


class Job(object):

    def __init__(self):
        self.image = None
        self.snap = None
        self.__load_job_data()

    def __parse_data_from_file(self, job_file):
        with open('settings.yml') as file_data:
            parsed_yaml = yaml.safe_load(file_data)
        return parsed_yaml

    def __load_job_data(self):
        job_files = glob.glob(JOBS_DIRECTORY + "/job_*.yml")
        try:
            # Take the first file if there are many
            parsed_yaml = self.__parse_data_from_file(job_files[0])
            self.image = Setting(parsed_yaml['image'])
            self.snap = Setting(parsed_yaml['snap'])
        except (IndexError, KeyError):
            pass

    def is_defined(self):
        if not self.image:
            return False
        if not self.snap:
            return False
        return True
