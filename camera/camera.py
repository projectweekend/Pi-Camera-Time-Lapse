import time
from picamera import PiCamera
from threading import Thread
from uploader import upload_file


class ConfigurableCamera(PiCamera):

    def __init__(self, job):
        super(ConfigurableCamera, self).__init__()
        self.__job = job
        self.__configure()

    def __set_resolution(self):
        try:
            resolution_x = self.__job.settings.resolution_x
            resolution_y = self.__job.settings.resolution_y
        except AttributeError:
            pass
        else:
            self.resolution = (resolution_x, resolution_y)

    def __set_ISO(self):
        try:
            self.ISO = self.__job.settings.ISO
        except AttributeError:
            pass

    def __set_brightness(self):
        try:
            self.brightness = self.__job.brightness
        except AttributeError:
            pass

    def __set_contrast(self):
        try:
            self.contrast = self.__job.settings.contrast
        except AttributeError:
            pass

    def __set_exposure_compensation(self):
        try:
            self.exposure_compensation = self.__job.settings.exposure_compensation
        except AttributeError:
            pass

    def __set_rotation(self):
        try:
            self.rotation = self.__job.settings.rotation
        except AttributeError:
            pass

    def __set_saturation(self):
        try:
            self.saturation = self.__job.settings.saturation
        except AttributeError:
            pass

    def __set_sharpness(self):
        try:
            self.sharpness = self.__job.settings.sharpness
        except AttributeError:
            pass

    def __set_shutter_speed(self):
        try:
            self.shutter_speed = self.__job.settings.shutter_speed
        except AttributeError:
            pass

    def __configure(self):
        self.__set_resolution()
        self.__set_ISO()
        self.__set_brightness()
        self.__set_contrast()
        self.__set_exposure_compensation()
        self.__set_rotation()
        self.__set_saturation()
        self.__set_sharpness()
        self.__set_shutter_speed()
        time.sleep(2)

    def time_lapse(self, output_file):
        quality = self.__job.settings.quality
        interval = self.__job.settings.snap_interval
        total = self.__job.settings.snap_total

        capture = self.capture_continuous(output_file, quality=quality)
        for i, file_name in enumerate(capture):
            Thread(target=upload_file, args=(file_name,)).start()
            if i == total - 1:
                self.__job.archive()
                break
            time.sleep(interval)
