import time
import yaml
import picamera
import utils
import uploader


with open('settings.yml') as settings_file:
    YML = yaml.safe_load(settings_file)
    IMAGE = utils.Settings(YML['image'])
    SNAP = utils.Settings(YML['snap'])


if __name__ == '__main__':
    with picamera.PiCamera() as camera:
        camera.resolution = (IMAGE.resolution_x, IMAGE.resolution_y)
        time.sleep(2)
        output_file = IMAGE.directory + '/img{counter:03d}.jpg'
        capture = camera.capture_continuous(output_file, quality=IMAGE.quality)
        for i, _ in enumerate(capture):
            if i == SNAP.total - 1:
                break
            time.sleep(SNAP.interval)
