#!/usr/bin/env python

import subprocess


def sudo(command_text):
    parts = ['sudo']
    parts.extend(command_text.split(command_text))
    subprocess.call(parts, shell=True)


def apt_get_install(package_name):
    command_text = "apt-get -y install {0}".format(package_name)
    sudo(command_text)


def main():
    # Install system dependencies
    sudo("apt-get update")
    sudo("apt-get -y upgrade")
    apt_get_install("upstart")
    apt_get_install("python-dev")
    apt_get_install("python-pip")

    # Setup the virtualenv
    subprocess.call(["pip", "install", "virtualenv"])
    subprocess.call(["virtualenv", "env", "--no-site-packages"])
    subprocess.call(["source", "./env/bin/activate"])
    subprocess.call(["pip", "install", "-r", "requirements.txt"])

    # Make default images folder
    subprocess.call(["mkdir", "/home/pi/images"])

    # Copy Upstart scripts
    subprocess.call(["cp", "upstart/dropbox-worker.conf", "/etc/init"])
    subprocess.call(["cp", "upstart/time-lapse.conf", "/etc/init"])

    print("Installation complete!")
    print("Please reboot your Raspberry Pi :)")


if __name__ == '__main__':
    main()
