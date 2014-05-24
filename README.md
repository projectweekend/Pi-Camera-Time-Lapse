## Install/Setup
The following instructions cover everything necessary to setup your Raspberry Pi for this project. I tried to script out a good chunk of system installation stuff to help keep things fairly simple. With that said, I welcome feedback about how to make this better.

#### Step 1: Clone this repository

```
git clone https://github.com/projectweekend/Pi-Camera-Time-Lapse.git
```

#### Step 2: Authorize Dropbox account
For automatic uploading of time-lapse images to Dropbox, you must authorize your account with the Pi Camera Time-Lapse app. I made the the following website to take you through the process and generate a key file you will need to save on your Raspberry Pi: [http://pi-camera-time-lapse.herokuapp.com/](http://pi-camera-time-lapse.herokuapp.com/). Once the `dropbox.txt` file is downloaded, save it the root of the project directory: `Pi-Camera-Time-Lapse/`.

#### Step 3: Install system stuff

```
cd Pi-Camera-Time-Lapse
sudo ./install_system.py
```

**NOTE:** When the command that installs [Upstart](http://upstart.ubuntu.com/) is executed, you will receive a warning. It will prompt you to type the following message to confirm the installation: `Yes, do as I say!`. You must type it exactly.


#### Step 4: Install project stuff

```
./install_project.py
```

**NOTE:** Do not run this step with `sudo`.

#### Step 5: Install Python libraries

```
source ./env/bin/activate
pip install -r requirements.txt
```

#### Step 6: Reboot

```
sudo reboot
```

## Making a time-lapse

Time-lapse sequences are controlled using job files written in [YAML](http://en.wikipedia.org/wiki/YAML). This file describes everything needed to execute the time-lapse. Job files must be saved in the directory `/home/pi/time-lapse/jobs` and prefixed with `job_`. If multiple files are found, they will be processed one at a time in alphabetical order.

#### Example job file

Name: `job_sunset_time_lapse.yml`

~~~yaml
snap:
    interval: 60
    total: 30
image:
    prefix: sunset_
    resolution_x: 2592
    resolution_y: 1944
    quality: 100
    iso: 400
    brightness: 50
    contrast: 0
    saturation: 0
    sharpness: 0
    shutter_speed: 0
    exposure_compensation: 0
    rotation: 0
~~~

* `snap.interval` - The number of seconds that should elapse between shots
* `snap.total` - The total number of pictures to take
* `image.prefix` - A custom file prefix added to each image file saved
* `image.quality` - Controls JPG quality (max: 100)
* `image.resolution_x` - The horizontal resolution of the output image (max: 2592)
* `image.resolution_y` - The vertical resolution of the output image (max: 1944)
