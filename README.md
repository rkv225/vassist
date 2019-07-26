# Raspberry Pi Virtual Assistant

### Some points::
- default audio device should be set to usb pnp device
- no capital letters should be used in firebase data
- remote should only be one word
- function name should have _ instead of spaces
- relay switches label should have _ in place of space

## List of Packages Used

- json
- firebase
- pico2wave tts
- LIRC
- Selenium
- wikipedia
- openweathermap
- beautifulsoup
- Scikit-Learn
- mpg321 player

## Installing Instructions

### Installing JSON:

pip install json

-------------------------------------------------------------------------
### Installing firebase:

pip install firebase

pip install python-firebase

References::
http://raspberrypi4u.blogspot.com/2017/12/raspberry-pi-iot-firebase-realtimedatabase.html
https://ozgur.github.io/python-firebase/

-------------------------------------------------------------------------

### Installing pico2wave TTS:

sudo apt-get install libttspico-utils
//invoking command
pico2wave -w lookdave.wav "Look Dave, I can see you're really upset about this." && aplay lookdave.wav

-------------------------------------------------------------------------
### Installing and Setting up LIRC: 

  $ sudo apt-get update
  $ sudo apt-get install lirc

  // Add the following lines to /etc/modules file
  lirc_dev
  lirc_rpi gpio_in_pin=18 gpio_out_pin=17

  // Add the following lines to /etc/lirc/hardware.conf file
  LIRCD_ARGS="--uinput --listen"
  LOAD_MODULES=true
  DRIVER="default"
  DEVICE="/dev/lirc0"
  MODULES="lirc_rpi"

  // Update the following line in /boot/config.txt
  dtoverlay=lirc-rpi,gpio_in_pin=18,gpio_out_pin=17

  // Update the following lines in /etc/lirc/lirc_options.conf
  driver    = default
  device    = /dev/lirc0

  $ sudo /etc/init.d/lircd stop
  $ sudo /etc/init.d/lircd start

  // Check status to make lirc is running
  $ sudo /etc/init.d/lircd status

  // Reboot before testing
  $ reboot

  // To test if lirc driver is working
  $ sudo /etc/init.d/lircd stop
  $ mode2 -d /dev/lirc0
  <press a key in remote and you should see multple lines like below>
  pulse 560
  space 1706
  pulse 535

  // to record a custom remote/register a remote device
  $ sudo /etc/init.d/lircd stop
  $ sudo irrecord -d /dev/lirc0 ~/lircd.conf
  // follow the instruction prompted by the above command carefully
  // at the end ~/lircd.conf file will be generated

  // backup the original lircd.conf
  $ sudo mv /etc/lirc/lircd.conf /etc/lirc/lircd_original.conf
  $ sudo cp ~/lircd.conf /etc/lirc/lircd.conf
  $ sudo /etc/init.d/lircd start

  // you can test if the recorded remote works by
  $ irsend SEND_ONCE <device-name> KEY_POWER
  $ irsend SEND_ONCE <device-name> KEY_VOLUMEUP


  REferences::
  http://www.lirc.org/
  https://gist.github.com/prasanthj/c15a5298eb682bde34961c322c95378b
  https://sites.google.com/site/marcobotprojects/my-projects/my-rasplex-video-player/settinguplircandtheirremotecontroller

------------------------------------------------------------------------
### Installing Selenium:

//make sure the chromium browser is up-to-date

sudo apt-get update
sudo apt-get install chromium-browser --yes

//install selenium

sudo pip install selenium

//install web driver

sudo apt-get install chromium-chromedriver

------------------------------------------------------------------------
### Installing wikipedia api:

pip install wikipedia

------------------------------------------------------------------------
### Installing OpenWeatherMap api:

pip install pyowm

References: https://github.com/csparpa/pyowm

------------------------------------------------------------------------

### Installing mpg321 player:

sudo apt-get -y install mpg321


------------------------------------------------------------------------
### Installing  beautifulsoup:

pip install requests
pip install beautifulsoup4

------------------------------------------------------------------------
### Installing Scikit-Learn:

pip install numpy

pip install pandas

sudo apt-get install gfortran libopenblas-dev liblapack-dev

pip install scikit-learn  /*can use sudo if doesn't work*/

pip install pickle-mixin
