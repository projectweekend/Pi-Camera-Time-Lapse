#!/usr/bin/env python

import sys
import time
import picamera
import settings
from settings import IMAGE, SNAP
import uploader


if __name__ == '__main__':

    with picamera.PiCamera() as camera:
        camera.resolution = (IMAGE.resolution_x, IMAGE.resolution_y)
        time.sleep(2)
        output_file = settings.IMAGES_DIRECTORY + '/img{counter:03d}.jpg'
        capture = camera.capture_continuous(output_file, quality=IMAGE.quality)
        for i, _ in enumerate(capture):
            if i == SNAP.total - 1:
                break
            time.sleep(SNAP.interval)
