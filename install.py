#!/usr/bin/env python

import subprocess


def main():
    # Install system dependencies
    subprocess.call(["apt-get", "update"])
    subprocess.call(["apt-get", "-y", "upgrade"])
    subprocess.call(["apt-get", "-y", "install", "upstart"])
    subprocess.call(["apt-get", "-y", "install", "python-dev"])
    subprocess.call(["apt-get", "-y", "install", "python-pip"])

    # Setup the virtualenv
    subprocess.call(["pip", "install", "virtualenv"])
    subprocess.call(["virtualenv", "env", "--no-site-packages"])

    # Make default images folder
    subprocess.call(["mkdir", "/home/pi/images"])

    # Copy Upstart scripts
    subprocess.call(["cp", "upstart/dropbox-worker.conf", "/etc/init"])
    subprocess.call(["cp", "upstart/time-lapse.conf", "/etc/init"])

    print("Installation complete!")
    print("Please reboot your Raspberry Pi :)")


if __name__ == '__main__':
    main()
