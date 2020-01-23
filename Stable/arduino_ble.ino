//20 Jan 2020
//Code written mostly by Yun Da, with reference to arduino ref page and sparksfun.
//BLE code was also referenced from https://makersportal.com/blog/2018/3/21/arduino-internet-of-things-part-2-lowering-the-power-consumption-of-the-atmega328p-breadboard-arduino-with-the-hm-10-bluetooth-module

#include <LowPower.h>
#include <SoftwareSerial.h>

int ble_rxd = 9; // ble transfer out
int ble_txd = 8; // ble receiver
int ble_vcc = 7; //Power in
int ble_gnd = 6; // Ground

//global variables (by hardware design)
const int sensorPin = 0;
const int ldrOUT = 11;
const int ldrGND = 12;
SoftwareSerial ble(9, 8); //RXD,TXD

int lightCal, lightVal, dk, lt, dk_num, lt_num, iter, darkval;

//ensure you start the device with the photodiode pointing at the LED when dark, not when bright.
const int light_threshold = 735;

//Things that you can update:
int scan_blink_iter = 12;
unsigned tml = SLEEP_8S;
unsigned tmd = SLEEP_8S;
//control how long between each blinking check
unsigned tmib = SLEEP_250MS;

int blinking_differential_thresh = 10;
int start_status = 0;
//General functions to be used:
//1- check if light is blinking
//We create a function/method that does a search for 5 seconds, checking if the LED is blinking, or in a steady state.

bool isblink(int scan_blink_iter, int dk_num, int lt_num, int iter)
{
  for (dk_num, lt_num, iter; iter < scan_blink_iter; iter++) {
    lightVal = analogRead(sensorPin);
    if (lightVal < light_threshold) {
      dk_num++;
      sleep_isblink();
    }
    else if (lightVal >= light_threshold) {
      lt_num++;
      sleep_isblink();
    }
  }
  //Possibility to add an exponential function here, that scales to a higher threshold as the number of cycles increase.
  if ((dk_num - lt_num) > blinking_differential_thresh) {
    start_status = 0;
    return 0;
  }
  else if ((dk_num - lt_num) < -blinking_differential_thresh) {
    start_status = 1;
    return 0;
  }
  else {
    //turn_on_ble;
    pinMode(ble_vcc, OUTPUT);
    pinMode(ble_gnd, OUTPUT);
    digitalWrite(ble_vcc, HIGH);
    digitalWrite(ble_gnd, LOW);
    delay(888);
    ble.write("error");
    ble.flush();
    delay(3000);
    pinMode(ble_vcc, INPUT); //turn off ble
    pinMode(ble_gnd, INPUT);
    return 1;
  }
}

//Sleep functions (no need to change)
void sleepl()
{
  //LowPower.idle(tml, ADC_OFF, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, SPI_OFF, USART0_OFF, TWI_OFF);
  LowPower.powerDown(tml, ADC_OFF, BOD_OFF);
}
void sleepd()
{
  //  LowPower.idle(tmd, ADC_OFF, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, SPI_OFF, USART0_OFF, TWI_OFF);
  LowPower.powerDown(tmd, ADC_OFF, BOD_OFF);
}
void sleep_isblink()
{
  LowPower.powerDown(tmib, ADC_OFF, BOD_OFF);
  //  LowPower.idle(tmib, ADC_OFF, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, SPI_OFF, USART0_ON, TWI_OFF);
}

void setup()
{
  ble.begin(9600);//9600 is the baud rate of the BLE.
  lightCal = analogRead(sensorPin);
  //we will take a single reading from the light sensor and store it in the lightCal
  //variable. This will give us a prelinary value to compare against in the loop
  darkval = analogRead(sensorPin);
  pinMode(ldrOUT, OUTPUT);
  pinMode(ldrGND, OUTPUT);

  pinMode(ble_vcc, OUTPUT); // Turn on BLE
  pinMode(ble_gnd, OUTPUT);
  digitalWrite(ble_vcc, HIGH);
  digitalWrite(ble_gnd, LOW); //Turn on BLE
  //Serial.begin(9600);
}

//START of main loop.
void loop()
{
  //Turn on the photoresistor components.
  pinMode(ldrOUT, OUTPUT);
  pinMode(ldrGND, OUTPUT);
  digitalWrite(ldrOUT, HIGH);
  digitalWrite(ldrGND, LOW);
  delay(500);
  lightVal = analogRead(sensorPin);
  if (lightVal < 100)
  {
    pinMode(ble_vcc, OUTPUT);//turn_on_ble;
    pinMode(ble_gnd, OUTPUT);
    digitalWrite(ble_vcc, HIGH);
    digitalWrite(ble_gnd, LOW);
    delay(888);
   // Serial.println("off");
    //Serial.flush();
    ble.write("first");
    ble.flush();     //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text
    delay(3000);
    }
    else if (lightVal > 99 and lightVal<200)
  {
    pinMode(ble_vcc, OUTPUT);//turn_on_ble;
    pinMode(ble_gnd, OUTPUT);
    digitalWrite(ble_vcc, HIGH);
    digitalWrite(ble_gnd, LOW);
    delay(888);
   // Serial.println("off");
    //Serial.flush();
    ble.write("second");
    ble.flush();     //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text
    delay(3000);
    }
    else if (lightVal > 199 and lightVal<300)
  {
    pinMode(ble_vcc, OUTPUT);//turn_on_ble;
    pinMode(ble_gnd, OUTPUT);
    digitalWrite(ble_vcc, HIGH);
    digitalWrite(ble_gnd, LOW);
    delay(888);
   // Serial.println("off");
    //Serial.flush();
    ble.write("third");
    ble.flush();     //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text
    delay(3000);
    }
    else if (lightVal > 299 and lightVal<400)
  {
    pinMode(ble_vcc, OUTPUT);//turn_on_ble;
    pinMode(ble_gnd, OUTPUT);
    digitalWrite(ble_vcc, HIGH);
    digitalWrite(ble_gnd, LOW);
    delay(888);
   // Serial.println("off");
    //Serial.flush();
    ble.write("fourth");
    ble.flush();     //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text
    delay(3000);
    }
    else if (lightVal > 399 and lightVal<500)
  {
    pinMode(ble_vcc, OUTPUT);//turn_on_ble;
    pinMode(ble_gnd, OUTPUT);
    digitalWrite(ble_vcc, HIGH);
    digitalWrite(ble_gnd, LOW);
    delay(888);
   // Serial.println("off");
    //Serial.flush();
    ble.write("fifth");
    ble.flush();     //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text
    delay(3000);
    }
    else if (lightVal > 499 and lightVal<600)
  {
    pinMode(ble_vcc, OUTPUT);//turn_on_ble;
    pinMode(ble_gnd, OUTPUT);
    digitalWrite(ble_vcc, HIGH);
    digitalWrite(ble_gnd, LOW);
    delay(888);
   // Serial.println("off");
    //Serial.flush();
    ble.write("sixth");
    ble.flush();     //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text
    delay(3000);
    }
    else if (lightVal > 599 and lightVal<700)
  {
    pinMode(ble_vcc, OUTPUT);//turn_on_ble;
    pinMode(ble_gnd, OUTPUT);
    digitalWrite(ble_vcc, HIGH);
    digitalWrite(ble_gnd, LOW);
    delay(888);
   // Serial.println("off");
    //Serial.flush();
    ble.write("seventh");
    ble.flush();     //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text
    delay(3000);
    }
    else if (lightVal > 699 and lightVal<800)
  {
    pinMode(ble_vcc, OUTPUT);//turn_on_ble;
    pinMode(ble_gnd, OUTPUT);
    digitalWrite(ble_vcc, HIGH);
    digitalWrite(ble_gnd, LOW);
    delay(888);
   // Serial.println("off");
    //Serial.flush();
    ble.write("eigth");
    ble.flush();     //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text
    delay(3000);
    }
    else if (lightVal > 799 and lightVal<900)
  {
    pinMode(ble_vcc, OUTPUT);//turn_on_ble;
    pinMode(ble_gnd, OUTPUT);
    digitalWrite(ble_vcc, HIGH);
    digitalWrite(ble_gnd, LOW);
    delay(888);
   // Serial.println("off");
    //Serial.flush();
    ble.write("ninth");
    ble.flush();     //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text
    delay(3000);
    }
    else if (lightVal > 899 and lightVal<1000)
  {
    pinMode(ble_vcc, OUTPUT);//turn_on_ble;
    pinMode(ble_gnd, OUTPUT);
    digitalWrite(ble_vcc, HIGH);
    digitalWrite(ble_gnd, LOW);
    delay(888);
   // Serial.println("off");
    //Serial.flush();
    ble.write("tenth");
    ble.flush();     //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text
    delay(3000);
    }
    
    else if (lightVal > 999 and lightVal<1100)
  {
    pinMode(ble_vcc, OUTPUT);//turn_on_ble;
    pinMode(ble_gnd, OUTPUT);
    digitalWrite(ble_vcc, HIGH);
    digitalWrite(ble_gnd, LOW);
    delay(888);
   // Serial.println("off");
    //Serial.flush();
    ble.write("max");
    ble.flush();     //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text
    delay(3000);
    }
    

  
  /*
  //Take a reading using analogRead() on sensor pin and store it in lightVal
  lightVal = analogRead(sensorPin);
  Serial.println(lightVal);
  Serial.flush();
  */
  if (start_status > 0)
  {
    while (isblink(scan_blink_iter, 0, 0, 0))
    {
      //return;
    }
  }
  else
  {
  }

lightVal = analogRead(sensorPin);
  
  if (lightVal < light_threshold) // Check if it is dark.
  {
    start_status = 0;
    pinMode(ldrOUT, INPUT); //Turn off LDR
    pinMode(ldrGND, INPUT); //Turn off LDR
    pinMode(ble_vcc, OUTPUT);//turn_on_ble;
    pinMode(ble_gnd, OUTPUT);
    digitalWrite(ble_vcc, HIGH);
    digitalWrite(ble_gnd, LOW);
    delay(888);
   // Serial.println("off");
    //Serial.flush();
    ble.write("off");
    ble.flush();     //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text
    delay(3000);
    pinMode(ble_vcc, INPUT); //Turn off BLE
    pinMode(ble_gnd, INPUT);
    sleepd(); sleepd(); sleepd(); sleepd(); sleepd(); sleepd(); sleepd(); sleepd();
  }
  else
  {
    start_status = 1;
    pinMode(ldrOUT, INPUT); //Turn off LDR
    pinMode(ldrGND, INPUT); //Turn off LDR
    pinMode(ble_vcc, OUTPUT); //turn_on_ble
    pinMode(ble_gnd, OUTPUT);//turn_on_ble
    digitalWrite(ble_vcc, HIGH);//turn_on_ble
    digitalWrite(ble_gnd, LOW);//turn_on_ble
    delay(888);
    ble.write("on");
    ble.flush();
    delay(3000);
    pinMode(ble_vcc, INPUT); //turn_off_ble;
    pinMode(ble_gnd, INPUT); //turn_off_ble;
    sleepl(); sleepl(); sleepl(); sleepl();
  }
}

/* For Future reference: For the peripheral to read and input and print out the commands.
  while (Serial.available() > 0)
     {
         comdata = Serial.readString();
         delay(15);
         Serial.print(comdata);
        Serial.println("");
     }
*/
