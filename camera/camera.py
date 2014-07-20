import time
from picamera import PiCamera
from threading import Thread
from uploader import upload_file, has_network_connection


class ConfigurableCamera(PiCamera):

    def __init__(self, job):
        super(ConfigurableCamera, self).__init__()
        self.__job = job
        self.__configure()
        self.__test_network()

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

    def __set_exposure_mode(self):
        try:
            self.exposure_mode = self.__job.settings.exposure_mode
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

    def __set_awb_mode(self):
        try:
            self.awb_mode = self.__job.settings.awb_mode
        except AttributeError:
            pass

    def __set_auto_upload(self):
        try:
            if self.__job.settings.auto_upload == "Off":
                self.auto_upload = False
        except AttributeError:
            self.auto_upload = True

    def __configure(self):
        self.__set_resolution()
        self.__set_ISO()
        self.__set_brightness()
        self.__set_contrast()
        self.__set_exposure_compensation()
        self.__set_exposure_mode()
        self.__set_rotation()
        self.__set_saturation()
        self.__set_sharpness()
        self.__set_shutter_speed()
        self.__set_awb_mode()
        self.__set_auto_upload()
        time.sleep(2)

    def __test_network(self):
        self.has_network_connection = has_network_connection()

    def time_lapse(self, output_file):
        quality = self.__job.settings.quality
        interval = self.__job.settings.snap_interval
        total = self.__job.settings.snap_total

        capture = self.capture_continuous(output_file, quality=quality)
        for i, file_name in enumerate(capture):
            if self.auto_upload and self.has_network_connection:
                Thread(target=upload_file, args=(file_name,)).start()
            if i == total - 1:
                self.__job.archive()
                break
            time.sleep(interval)
