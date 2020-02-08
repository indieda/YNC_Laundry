from urllib.request import urlopen
from datetime import datetime
import re
import smtplib
import sm
import socket

# Setup our login credentials
from_address = 'HalcyonLaundry@gmail.com'
to_address = 'HalcyonLaundry@gmail.com'
subject = str(datetime.now()) + ' ' + 'HalcyonLaundry Cendana IP'
username = 'HalcyonLaundry@gmail.com'
password = 'Yundachua1'

# Setup where we will get our IP address
url = 'http://checkip.dyndns.org'
print ("Our chosen IP address service is ", url)

# Open up the url, then read the contents, and take away our IP address
request = urlopen(url).read().decode('utf-8')
# We extract the IP address only
ourIP = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", request)
ourIP = str(ourIP)
internalIP = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
internalIP.connect(("8.8.8.8",80))
ip_to_send = str(internalIP.getsockname()[0])
print("The internal ip is:", ip_to_send)
internalIP.close()
print ("Our public IP address is: ", ourIP)

def send_email(ip_to_send):
# Body of the email
    body_text = ip_to_send + ' is our YNC_Laundry IP address' + ourIP + "is our public external ip"
    msg = '\r\n'.join(['To: %s' % to_address, 'From: %s' % from_address, 'Subject: %s' % subject, '', body_text])

    # Actually send the email!
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls() # Our security for transmission of credentials
    server.login(username,password)
    server.sendmail(from_address, to_address, msg)
    server.quit()
    print ("Our email has been sent!")

# Open up previous IP address (last_ip.txt) and extract contents
with open('/home/pi/Documents/last_ip.txt', 'rt') as last_ip:
    last_ip = last_ip.read() # Read the text file

# Check to see if our IP address has really changed
if last_ip == ourIP: #this will always send out. Deliberately not made it last_ip = ip_to_send so that it will always send!
    print("Our IP address has not changed.")
else:
    print ("We have a new IP address.")
    with open('/home/pi/Documents/last_ip.txt', 'wt') as last_ip:
        last_ip.write(ip_to_send)
        last_ip.close()
    print ("We have written the new IP address to the text file.")
    try:
        send_email(ip_to_send)
    except:
        pass
