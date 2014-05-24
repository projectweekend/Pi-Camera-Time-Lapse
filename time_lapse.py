#!/usr/bin/env python

import time
from camera import ConfigurableCamera
from threading import Thread
from uploader import upload_file
from settings import Job, IMAGES_DIRECTORY


def main():

    job = Job()
    if job.exists():

        interval = job.snap_settings.interval
        total = job.snap_settings.total
        quality = job.image_settings.quality
        file_prefix = job.image_settings.prefix
        output_file = IMAGES_DIRECTORY + '/' + file_prefix + '_{counter:03d}.jpg'

        with ConfigurableCamera(job=job) as camera:
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
