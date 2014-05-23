#!/usr/bin/env python

import time
import picamera
from settings import Job, IMAGES_DIRECTORY


def main():
    job = Job()
    if job.exists():
        resolution_x = job.image_settings.resolution_x
        resolution_y = job.image_settings.resolution_y
        image_quality = job.image_settings.quality
        snap_interval = job.snap_settings.interval
        snap_total = job.snap_settings.total
        file_prefix = job.image_settings.prefix
        output_file = IMAGES_DIRECTORY + '/' + file_prefix + '_{counter:03d}.jpg'
        with picamera.PiCamera() as camera:
            camera.resolution = (resolution_x, resolution_y)
            time.sleep(2)
            capture = camera.capture_continuous(output_file, quality=image_quality)
            for i, _ in enumerate(capture):
                if i == snap_total - 1:
                    job.archive()
                    break
                time.sleep(snap_interval)


if __name__ == '__main__':
    while True:
        main()
