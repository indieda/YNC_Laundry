from urllib.request import urlopen
import re
import smtplib
import sm

# Setup our login credentials
from_address = 'HalcyonLaundry@gmail.com'
to_address = 'HalcyonLaundry@gmail.com'
subject = 'Pi IP'
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
print ("Our IP address is: ", ourIP)

def send_email(ourIP):
# Body of the email
    body_text = ourIP + ' is our YNC_Laundry IP address'
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
if last_ip == ourIP:
    print("Our IP address has not changed.")
else:
    print ("We have a new IP address.")
    with open('/home/pi/Documents/last_ip.txt', 'wt') as last_ip:
        last_ip.write(ourIP)
    print ("We have written the new IP address to the text file.")
    send_email(ourIP)
