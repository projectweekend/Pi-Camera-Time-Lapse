## Getting started

The following instructions cover everything necessary to setup your Raspberry Pi for this project. I tried to script out a good chunk of system installation stuff to help keep things fairly simple. With that said, I welcome feedback about how to make this better.

#### Step 1: Clone this repository

`git clone https://github.com/projectweekend/Pi-Camera-Time-Lapse.git`

#### Step 2: Install system requirements

```
cd Pi-Camera-Time-Lapse
sudo ./install.py
```

#### Step 3: Install project requirements

```
source ./env/bin/activate
pip install -r requirements.txt
```

#### Step 4: Reboot

```
sudo reboot
```
