#include <SoftwareSerial.h>
#include <LowPower.h>

SoftwareSerial mySerial(7, 8); // RX, TX
int vcc = 5;
int gnd = 4;
void setup()
 {
     mySerial.begin(9600);
     pinMode(vcc,OUTPUT);
     pinMode(gnd,OUTPUT);
     digitalWrite(5,HIGH);
     digitalWrite(gnd,LOW);
     Serial.begin(9600);
 }

void loop()
 {
Serial.write("looped");
pinMode(vcc,OUTPUT);
pinMode(gnd,OUTPUT);
digitalWrite(vcc,HIGH);
digitalWrite(gnd,LOW);
delay(500);

//delay(2000);
/*
if (mySerial.available() >0) // This runs once only, on the first connect. To print out onto serial monitor whatever I'm receving from BLE. 

{
while (mySerial.available()>0) //softwareserial's read is char by char. While make sure everything is read.
{
  Serial.write(mySerial.read()); 
}
Serial.write("Listening"); // delete after deploy

mySerial.write("light");
mySerial.flush();
delay(3000);

for (int i = 0; i < 4; i++) {
mySerial.write("hello");
mySerial.flush();
mySerial.write(i);
mySerial.flush();
Serial.write("printed hello ");
Serial.print(i);
Serial.flush();
delay(1000);
}



pinMode(vcc,INPUT);
pinMode(gnd,INPUT);
delay(1000);
}

*/


/*
//To delete
for (int i = 0; i < 4; i++) {
mySerial.write("hello\n");
mySerial.flush();
mySerial.write(i);
mySerial.flush();
Serial.write("printed hello ");
Serial.print(i);
Serial.flush();
delay(1000);
}
*/

mySerial.write("on");
mySerial.flush();
Serial.write("printed hello ");
Serial.flush();
Serial.flush();
delay(3000);

//Part 2 Checks if the BLE module is connected.
/*
if (mySerial.isListening())
{
  Serial.write("Listening");
  mySerial.write("hello");
mySerial.flush();
pinMode(vcc,OUTPUT);
pinMode(gnd,OUTPUT);
digitalWrite(vcc,HIGH);
digitalWrite(gnd,LOW);
delay(1000);
continue; 
  }
*/


//Part 3 Checks if there's anything being received on subsequent loops after the first one where "connected" is printed.
/*
while (mySerial.available()>0)
{
  Serial.write(mySerial.read());
}
Serial.write("Nothing in mySerial");
*/

//Part 4

pinMode(vcc,INPUT);
pinMode(gnd,INPUT);
LowPower.powerDown(SLEEP_4S,ADC_OFF,BOD_OFF);


  /*
     while (Serial.available() > 0)  
     {
         comdata = Serial.readString();
         delay(15);
         Serial.print(comdata);
         Serial.println("");
         mySerial.print(Serial.readString());
     }

while (Serial.available() > 0)  
     {
         comdata = Serial.readString();
         delay(15);
         Serial.print(comdata);
         Serial.println("");
     }
     
     while (mySerial.available() > 0)
     {
      comdata = mySerial.readString();
         delay(15);
         Serial.print(comdata);
         Serial.println("");
     }
     delay(1000);
 */
 }
