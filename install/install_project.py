#!/usr/bin/env python

import subprocess


def main():
    # Setup the virtualenv
    subprocess.call(["virtualenv", "env", "--no-site-packages"])

    # Make default images folder
    subprocess.call(["mkdir", "-p", "/home/pi/time-lapse/images"])
    subprocess.call(["mkdir", "-p", "/home/pi/time-lapse/jobs"])
    subprocess.call(["mkdir", "-p", "/home/pi/time-lapse/jobs/archive"])


if __name__ == '__main__':
    main()
