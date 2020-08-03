# YNC_Laundry



Hello! Welcome to the Yale-NUS College Laundry Codebase.

##### Table of Contents  
[Project Overview](#project-overview)
[**SOFTWARE**](#software)  
[Frontend](#frontend)  
[Backend](#backend)  
[Flask_App](#flask-python-web-app-which-interfaces-with-gunicorn-and-nginx-for-load-balancer)  
[**HARDWARE**](#hardware)  

## Project Overview

This readme should be read alongside the writeup over at: https://chuayunda.com/2020/02/25/yale-nus-smart-laundry/

**The folders: ```Deployed``` and ```Website``` are both live on the systems at Cendana.**

Original Repository by Shardul Saptoka Yale-NUS College '20, and heavily edited by Yun Da, Yale-NUS College '22

## Software
<https://github.com/indieda/YNC_Laundry/blob/master/README.md#software>

## Frontend
<https://github.com/indieda/YNC_Laundry/blob/master/README.md#frontend>
If you're interested in frontend
1. For what's being displayed on the webpage using the HTML: You'll want to head over to ```~/website/app/templates``` In there, you'll find the 3 html files which will be loaded when you head over to the webpage at laundry.chuayunda.com
2. For the HTML code to get the status data from the flask web app: edit the HTML's javascript, and ```/website/app/routes.py```. The flask app's home folder is in ```~/website/app```

## Backend
<https://github.com/indieda/YNC_Laundry/blob/master/README.md#backend>
If you're interested in how data gets sent from the laundry room to the web server: 
1. The raspberry pi code can be accessed at: ```~/Deployed/pi_central.py```
2. Arduino code is found at: ```~/Deployed/10_Feb_2020.ino```

## Flask Python web app (Which interfaces with Gunicorn and NGINX for load balancer)
https://github.com/indieda/YNC_Laundry/blob/master/README.md#flask-python-web-app-which-interfaces-with-gunicorn-and-nginx-for-load-balancer

1. We used to use SQLalchemy but I found it too clunky with flask. We're now using a json to store the status data, and send them around the app. ```~/website/app/status_db.json```
2. With regard to the weekly forecasting features, the script doing that can be accessed at: ```~/website/app/upload_gsheets.py```. I intend to run it with a cron job and just read from the ```~/website/app/status_db.json``` file and update a gsheet automatically to keep a proper log of all the events that happened, where it can be exported to R or some other program for further processing.


<https://github.com/indieda/YNC_Laundry/blob/master/README.md#hardware>
## Hardware
Arduino pro mini 8MHz
https://www.aliexpress.com/item/32672852945.html?spm=a2g0s.9042311.0.0.5a504c4dVc4d6i
AT-09 BLE module
https://www.aliexpress.com/item/32820135156.html?spm=a2g0s.9042311.0.0.5a504c4dVc4d6i
Raspberry pi 4 2GB

Instructions:
1. Upon receiving BLE chip, download Arduino IDE, plug in using USB to TTL https://www.aliexpress.com/item/32831329095.html?spm=a2g0s.9042311.0.0.5a504c4dVc4d6i from Mac directly to the BLE chip and do the following through the serial monitor of the Arduino IDE (Magnifying glass with a + symbol on the top right hand corner of the IDE):

AT Commands to run on the AT+09
Change transmission power (0 [-23] is lowest, 3 [+6dB] is highest): AT+POWE3
Change name: AT+NAMEYNC_Laundry_3-6
Check MAC Addr (This address will be used on the python script to check for its sensor readings): AT+LADDR
Check Peripheral (0 is peripheral): AT+ROLE

Light levels for arduino:
735 for washer 6 and 5, not sure yet for washer 3

Problems:
1. Cannot send numerical lightVal over BLE to Raspberry Pi using UTF-8
2. The Bluepy python module runnin gon the Raspberry Pi 4 gets into a bad state quite quickly, so I used crontab to restart the script every 10 minutes.
3. Washer 3 gives out error instead of AVAILABLE/UNAVAILABLE often enough.
