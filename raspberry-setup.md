# How to set up Raspberry Pi

## Create Raspbian OS micro SD memory card

1. Download Raspbian image from [Raspberry Pi official Homepage](https://www.raspberrypi.org/downloads/)
2. Unpack yyyy-mm-dd-raspbian-stretch.zip. Use 7zip if your unzip program does not work. (Original zip/unzip program can not handle file size > 4GB)
3. Prepare micro SD memory card 16GB or bigger (up to 32GB is supported ?).
4. Attach the SD card to PC (using adapter)
5. In case of Linux, execute following commands. /dev/sdb can be /dev/sdc or /dev/sdd ... depending on your configuration

```
$sudo umount /dev/sdb1
$sudo dd if=2017-09-07-raspbian-stretch.img of=/dev/sdb bs=1M status=progress
```
dd command writes the boot sector and overwrites file systems.
In case of Windows, there are several programs that can do same.

- Etcher <https://www.raspberrypi.org/documentation/installation/installing-images/>
- Win32DiskImager <https://www.raspberrypi.org/documentation/installation/installing-images/windows.md>


2017-09-07 raspbian image is about 5GByte, and it tooks 1053sec for one of the SD, and 633sec for another.


## Initial set up

1. Insert the micro SD memory to Raspberry Pi
2. Connect USB Keyboard, Mouse and HDMI Display
3. Power On. (Raspberry Pi does not have a Power switch, supply power from USB connector)
4. Execute raspi-config (from GUI or ```$sudo raspi-config```)

    - Extend file system
    - Update the password of User: pi (default user name)
    - Enable ssh


## Need to care

- USB power supply must be 1.2A minimum, 2.5A is recommended
- In order to shut down, use GUI menu or ```$sudo poweroff```

## Avahi and SSH

With Avahi service, raspberry Pi can be accessed with hostname instead of IP address if both of server and client are connected to same router.

Other computer (Linux, Windows) can access Raspberry-pi via SSH, if SSH is enabled.

- Check current hostname (default: raspberrypi)

```
$ hostname
```

- Change hostname. Edit /etc/hosts and /etc/hostname

```
$ sudo gedit /etc/hosts
$ sudo gedit /etc/hostname
```

- Enable SSH server on Raspberry Pi via raspi-config (GUI or CLI)

- Reboot the system and check hostname again

```
$ sudo reboot
$ hostname
```

- Check if Raspberry-Pi can be accessed using hostname (From other machine)

```
$ ping raspberry-pi's-new-hostname
$ ssh pi@raspberry-pi's-new-hostname
```
