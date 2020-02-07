# YNC_Laundry

HARDWARE:
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


Problems:
1. Cannot send numerical lightVal over BLE to Raspberry Pi using UTF-8
2. The Bluepy python module runnin gon the Raspberry Pi 4 gets into a bad state quite quickly, so I used crontab to restart the script every 10 minutes.
3.
