#!/usr/bin/env python

import subprocess


def main():
    # Setup the virtualenv
    subprocess.call(["pip", "install", "virtualenv"])
    subprocess.call(["virtualenv", "env", "--no-site-packages"])

    # Make default images folder
    subprocess.call(["mkdir", "-p", "/home/pi/time-lapse/images"])
    subprocess.call(["mkdir", "-p", "/home/pi/time-lapse/jobs"])
    subprocess.call(["mkdir", "-p", "/home/pi/time-lapse/jobs/archive"])

    print("Installation is complete!")
    print("Next steps...")
    print("1.) activate the virtualenv: source ./env/bin/activate")
    print("2.) install requirements: pip install -r requirements.txt")
    print("3.) reboot your Pi: sudo reboot")


if __name__ == '__main__':
    main()
