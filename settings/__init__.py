import shutil
import glob
import yaml


DROPBOX_TOKEN_FILE = "./dropbox.txt"
WORKING_DIRECTORY = "/home/pi/time-lapse"
IMAGES_DIRECTORY = WORKING_DIRECTORY + "/images"
JOBS_DIRECTORY = WORKING_DIRECTORY + "/jobs"
JOBS_ARCHIVE = JOBS_DIRECTORY + "/archive"


class Setting(object):

    def __init__(self, settings_dict):
        self.__dict__.update(settings_dict)


class Job(object):

    def __init__(self):
        self.__load_job_file()
        self.__parse_job_data()

    def __load_job_file(self):
        job_files = glob.glob(JOBS_DIRECTORY + "/job_*.yml")
        try:
            self.job_file = job_files[0]
        except IndexError:
            self.job_file = None

    def __parse_job_data(self):
        try:
            with open(self.job_file) as file_data:
                parsed_yaml = yaml.safe_load(file_data)
                self.image_settings = Setting(parsed_yaml['image'])
                self.snap_settings = Setting(parsed_yaml['snap'])
        except TypeError:
            self.image_settings = None
            self.snap_settings = None

    def exists(self):
        if not self.job_file:
            return False
        return True

    def archive(self):
        shutil.move(self.job_file, JOBS_ARCHIVE)
