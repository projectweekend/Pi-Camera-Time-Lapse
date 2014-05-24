import time
from picamera import PiCamera


# iso = job.image_settings.iso
# brightness = job.image_settings.brightness
# contrast = job.image_settings.contrast
# saturation = job.image_settings.saturation
# sharpness = job.image_settings.sharpness
# shutter_speed = job.image_settings.shutter_speed
# exposure_compensation = job.image_settings.exposure_compensation
# rotation = job.image_settings.rotation
# resolution_x = job.image_settings.resolution_x
# resolution_y = job.image_settings.resolution_y


class ConfigurableCamera(PiCamera):

    def __init__(self, job):
        super(ConfigurableCamera, self).__init__()
        self.__job = job
        self.__configure()

    def __set_resolution(self):
        resolution_x = self.__job.settings.resolution_x
        resolution_y = self.__job.settings.resolution_y
        if resolution_x and resolution_y:
            self.resolution = (resolution_x, resolution_y)

    def __configure(self):
        self.__set_resolution()
        time.sleep(2)

