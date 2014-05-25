#!/usr/bin/env python

from camera import ConfigurableCamera
from settings import Job, IMAGES_DIRECTORY


def main():

    job = Job()
    if job.exists():
        file_prefix = job.image_settings.prefix
        output_file = IMAGES_DIRECTORY + '/' + file_prefix + '_{counter:03d}.jpg'
        with ConfigurableCamera(job=job) as camera:
            camera.time_lapse(output_file)


if __name__ == '__main__':
    while True:
        main()
