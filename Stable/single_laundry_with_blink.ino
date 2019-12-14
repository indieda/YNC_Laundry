//12 Dec 2019
//Code written mostly by Yun Da, with reference to arduino ref page and sparksfun.

#include "LowPower.h"

//global variables
const int sensorPin = 0;
int lightCal, lightVal, dk, lt, dk_num, lt_num, iter, darkval;

//ensure you start the device with the photodiode pointing at the LED when dark, not when bright.
const int light_threshold = 150;

//Things that you can update:
int scan_blink_iter = 20;
unsigned tml = SLEEP_8S;
unsigned tmd = SLEEP_8S;
//control how long between each blinking check
unsigned tmib = SLEEP_250MS;


int blinking_differential_thresh = 8;

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
    return 0;
  }
  else if ((dk_num - lt_num) < -blinking_differential_thresh) {
    return 0;
  }
  else {
    Serial.write("b1\n");
    return 1;
  }
}

//Sleep functions (no need to change)
void sleepl()
{
//  LowPower.idle(tml, ADC_OFF, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, SPI_OFF, USART0_ON, TWI_OFF);
LowPower.powerDown(tml, ADC_OFF, BOD_OFF);
}
void sleepd()
{
//  LowPower.idle(tmd, ADC_OFF, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, SPI_OFF, USART0_ON, TWI_OFF);
LowPower.powerDown(tmd, ADC_OFF, BOD_OFF);
}
void sleep_isblink()
{
  LowPower.idle(tmib, ADC_OFF, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, SPI_OFF, USART0_ON, TWI_OFF);
}

void setup()
{
  // We'll set up the LED pin to be an output.
  //9600 is the baud rate of the BLE.
  Serial.begin(9600);
  //  pinMode(ledPin, OUTPUT);
  //  lightCal = analogRead(sensorPin);
  //we will take a single reading from the light sensor and store it in the lightCal
  //variable. This will give us a prelinary value to compare against in the loop
  //darkval = analogRead(sensorPin);
}

//START of main loop.
void loop()
{
  //Take a reading using analogRead() on sensor pin and store it in lightVal
  while (isblink(scan_blink_iter, 0, 0, 0)) {
  }

  lightVal = analogRead(sensorPin);
  //  Serial.println(lightVal);
  // Check if it is dark.
  if (lightVal < light_threshold)
  {
    Serial.write("d1\n");
    //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text 
    Serial.flush();
    sleepd(); sleepd(); sleepd(); sleepd(); sleepd(); sleepd(); sleepd();
  }
  else
  {
    Serial.write("l1\n");
    Serial.flush();
    sleepl(); sleepl();
  }
}

// For Future reference: For the peripheral to read and input and print out the commands.
//  while (Serial.available() > 0)
//     {
//         comdata = Serial.readString();
//         delay(15);
//         Serial.print(comdata);
//        Serial.println("");
//     }
