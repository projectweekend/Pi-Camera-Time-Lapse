#!/usr/bin/env python

import subprocess


def main():
    # Install system dependencies
    subprocess.call(["apt-get", "update"])
    subprocess.call(["apt-get", "-y", "upgrade"])
    subprocess.call(["apt-get", "-y", "--force-yes", "install", "upstart"])
    subprocess.call(["apt-get", "-y", "install", "python-dev"])
    subprocess.call(["apt-get", "-y", "install", "python-pip"])
    subprocess.call(["pip", "install", "virtualenv"])

    # Copy Upstart scripts
    subprocess.call(["cp", "upstart/dropbox-uploader.conf", "/etc/init"])
    subprocess.call(["cp", "upstart/time-lapse.conf", "/etc/init"])

    print("Next steps...")
    print("1.) run the install project script: ./install_project.py")


if __name__ == '__main__':
    main()
