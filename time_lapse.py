#!/usr/bin/env python

import time
import picamera
from threading import Thread
from uploader import upload_file
from settings import Job, IMAGES_DIRECTORY


def main():
    job = Job()
    if job.exists():
        resolution_x = job.image_settings.resolution_x
        resolution_y = job.image_settings.resolution_y
        quality = job.image_settings.quality
        interval = job.snap_settings.interval
        total = job.snap_settings.total
        file_prefix = job.image_settings.prefix
        output_file = IMAGES_DIRECTORY + '/' + file_prefix + '_{counter:03d}.jpg'
        with picamera.PiCamera() as camera:
            camera.resolution = (resolution_x, resolution_y)
            time.sleep(2)
            capture = camera.capture_continuous(output_file, quality=quality)
            for i, file_name in enumerate(capture):
                Thread(target=upload_file, args=(file_name,)).start()
                if i == total - 1:
                    job.archive()
                    break
                time.sleep(interval)


if __name__ == '__main__':
    while True:
        main()
