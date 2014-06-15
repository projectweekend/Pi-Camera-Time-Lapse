## Installation & Setup
The following instructions cover everything necessary to setup your Raspberry Pi for this project. I tried to script out a good chunk of system installation stuff to help keep things fairly simple. With that said, I welcome feedback about how to make this better.

#### Step 1: Clone this repository

```
git clone https://github.com/projectweekend/Pi-Camera-Time-Lapse.git
```

#### Step 2: Authorize Dropbox account
To automatically upload time-lapse images to Dropbox, you must authorize your account with the Pi Camera Time-Lapse Dropbox app. I made the the following website to handle this process and generate a key file you will need to save on your Raspberry Pi: [http://pi-camera-time-lapse.herokuapp.com/](http://pi-camera-time-lapse.herokuapp.com/). Once the `dropbox.txt` file is downloaded, save it the root of the project directory: `Pi-Camera-Time-Lapse/`.

#### Step 3: Run install script

From the project directory `Pi-Camera-Time-Lapse/`, run the following command:

```
./install.sh
```

**NOTE:** This step will probably take several minutes to complete. When the script starts to install [Upstart](http://upstart.ubuntu.com/), you will receive a warning message. It will prompt you to type the following message to confirm the installation: `Yes, do as I say!`. You must type it exactly.

#### Step 4: Reboot

```
sudo reboot
```

-------------------------------------------------------------------------------

## Making a time-lapse

Time-lapse sequences are controlled using job files written in [YAML](http://en.wikipedia.org/wiki/YAML). This file describes everything needed to execute the time-lapse. Job files must be saved in the directory `/home/pi/time-lapse/jobs` and prefixed with `job_`. If multiple files are found, they will be processed one at a time. When a time-lapse has completed, the job file will be moved into the archive folder: `/home/pi/time-lapse/jobs/archive`.

The `time-lapse` service runs in the background as an Upstart job. As soon as it finds a job file, in the directory referenced above, it will load those configurations and begin taking photos. Since there is no image preview, it's best to run a couple test images on your subject before commiting to a full time-lapse job. To do this, simply save a job file with a `snap_total` of 1. When the resulting image shows up in Dropbox, review it, tweak settings, and repeat until you get what you want.

#### Example job file

Name: `job_sunset_time_lapse.yml`

~~~yaml
snap_interval: 60
snap_total: 30
file_prefix: sunset_
resolution_x: 2592
resolution_y: 1944
quality: 100
ISO: 400
brightness: 50
contrast: 0
saturation: 0
sharpness: 0
shutter_speed: 0
exposure_compensation: 0
rotation: 0
~~~

Each of the configurable options in the job file corresponds to a setting in the [picamera.PiCamera](http://picamera.readthedocs.org/en/latest/api.html#picamera.PiCamera) object. Any setting not specified in the job file will use its default value in *picamera.PiCamera*.

If you want to disable automatic Dropbox uploading, add the following line to the config file:

```
auto_upload: Off
```
