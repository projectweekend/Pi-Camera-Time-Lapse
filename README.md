## Getting started
The following instructions cover everything necessary to setup your Raspberry Pi for this project. I tried to script out a good chunk of system installation stuff to help keep things fairly simple. With that said, I welcome feedback about how to make this better.

#### Step 1: Clone this repository

`git clone https://github.com/projectweekend/Pi-Camera-Time-Lapse.git`

#### Step 2: Authorize Dropbox account
For automatic uploading of time-lapse images to Dropbox, you must authorize your account with the Pi Camera Time-Lapse app. I made the the following website to take you through the process and generate a key file you will need to save on your Raspberry Pi: [http://pi-camera-time-lapse.herokuapp.com/](http://pi-camera-time-lapse.herokuapp.com/). Once the `dropbox.txt` file is downloaded, save it the root of the project directory: `Pi-Camera-Time-Lapse/`.

#### Step 3: Install system requirements

```
cd Pi-Camera-Time-Lapse
sudo ./install.py
```

**NOTE:** When the command that installs [Upstart](http://upstart.ubuntu.com/) is executed, you will receive a warning. It will prompt you to type the following message to confirm the installation: `Yes, do as I say!`. You must type it exactly.


#### Step 4: Install project requirements

```
source ./env/bin/activate
pip install -r requirements.txt
```

#### Step 5: Reboot

```
sudo reboot
```
