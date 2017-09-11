# Ubuntu 16.04 with XRDP and MATE. Version 2

## rattydave/docker-ubuntu-xrdp-mate-custom:latest points to v2

A virtual desktop docker conainer with persistant user information.

This image is automatically rebuilt when updates are realeased for Ubuntu.

Contents:
Ubuntu 16.04
Mate Desktop (ubuntu repo)
XRDP built from source
XRPDXORG built from source
tightvncserver (ubuntu repo)
X11vnc (ubuntu repo)
openssh-server (always useful)
Custom xrdp.ini script

Reasons for choosing the souce of XRDP and XRDPXORG over the repo versions is that the display can resized. Also xorg is far more effecient at memory and processing. 

```
docker run -d --name RattyDAVEv2 \
           -p 3389:3389 \
           -p 2222:22 \
           -v %LOCAL_PATH_TO_CREATEUSERS.TXT_FILE%:/root/createusers.txt \
           -v %LOCAL_PATH_TO_HOME_DIRECTORY%:/home \
           -dit --restart unless-stopped \
           rattydave/docker-ubuntu-xrdp-mate-custom:latest
```

Replace %LOCAL_PATH_TO_CREATEUSERS.TXT_FILE% with the local filename of the createusers file.
Replace %LOCAL_PATH_TO_HOME_DIRECTORY% with the local directory of the /home directorys.
You do not need to publish port 22 only use if needed.

This file contains 3 fields (username:password:is_sudo). Where username is the login id. Password is the password. is_sudo does the user have sudo access(only Y is recognised).

Example

```
mickey:mouse:N
daisy:duke:Y
dog:flash:n
morty:rick:wubba
```
In this example 4 users will be created and only daisy will have sudo rights.

At every reboot it will check this file and ADD any new users.

Example of a working command line.
```
docker run -d --name RattyDAVEv2 \
           -p 3389:3389 -p 3389:22 \
           -v /root/createusers.txt:/root/createusers.txt \
           -v /root/home:/home \
           -dit --restart unless-stopped \
           rattydave/docker-ubuntu-xrdp-mate-custom:latest
```