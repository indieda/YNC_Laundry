# YNC_Laundry

HARDWARE:
Arduino pro mini 8MHz
https://www.aliexpress.com/item/32672852945.html?spm=a2g0s.9042311.0.0.5a504c4dVc4d6i
AT-09 BLE module
https://www.aliexpress.com/item/32820135156.html?spm=a2g0s.9042311.0.0.5a504c4dVc4d6i
Raspberry pi 4 2GB

Problems:
1. Cannot send numerical lightVal over BLE to Raspberry Pi using UTF-8
2. The Bluepy python module runnin gon the Raspberry Pi 4 gets into a bad state quite quickly, so I used crontab to restart the script every 10 minutes.
3.
