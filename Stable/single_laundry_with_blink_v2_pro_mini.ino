//12 Dec 2019
//Code written mostly by Yun Da, with reference to arduino ref page and sparksfun.

#include <LowPower.h>
#include <SoftwareSerial.h>

#define ble_tx 9 // ble transfer out
#define ble_rx 8 // ble receiver
#define ble_vcc 7 //Power in
#define ble_gnd 6 // Ground

//global variables (by hardware design)
const int sensorPin = 0;
const int ldrOUT = 11;
const int ldrGND = 12;
SoftwareSerial ble(8,9);

int lightCal, lightVal, dk, lt, dk_num, lt_num, iter, darkval;
unsigned message;

//ensure you start the device with the photodiode pointing at the LED when dark, not when bright.
const int light_threshold = 150;


//Things that you can update:
int scan_blink_iter = 20;
unsigned tml = SLEEP_1S;
unsigned tmd = SLEEP_1S;
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
    Serial.write("b1");
    return 1;
  }
}





unsigned bluetooth_init(char message) {
 Serial.write(message);
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
//LowPower.powerDown(tmib, ADC_OFF, BOD_OFF);
  LowPower.idle(tmib, ADC_OFF, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, SPI_OFF, USART0_ON, TWI_OFF);
}

void setup()
{
  // We'll set up the LED pin to be an output.
  //9600 is the baud rate of the BLE.
  Serial.begin(9600);
  //  pinMode(ledPin, OUTPUT);
  lightCal = analogRead(sensorPin);
  //we will take a single reading from the light sensor and store it in the lightCal
  //variable. This will give us a prelinary value to compare against in the loop
  //darkval = analogRead(sensorPin);
  pinMode(ldrOUT,OUTPUT);
  pinMode(ldrGND,OUTPUT);

  pinMode(ble_vcc,OUTPUT);
  pinMode(ble_gnd,OUTPUT);
  digitalWrite(ble_vcc,HIGH);
  digitalWrite(ble_gnd,LOW);


}

//START of main loop.
void loop()
{
  //Turn on the photoresistor components.
  pinMode(ldrOUT,OUTPUT);
  pinMode(ldrGND,OUTPUT);
  digitalWrite(ldrOUT,HIGH);
  digitalWrite(ldrGND,LOW);
  
  //Take a reading using analogRead() on sensor pin and store it in lightVal
  while (isblink(scan_blink_iter, 0, 0, 0)) {
  }
  lightVal = analogRead(sensorPin);
  Serial.println(lightVal);
  // Check if it is dark.
  if (lightVal < light_threshold)
  {
    Serial.write("d1");
    //This is an extremely important statement to ensure that all the bytes are sent over bluetooth before entering sleep mode. Without it, you wouldn't be able to decode the messages properly. Read for more: https://arduino.stackexchange.com/questions/14411/low-power-library-messing-up-serial-text 
    Serial.flush();
    delay(2000);
    pinMode(ldrOUT,INPUT); //Turn off LDR
    pinMode(ldrGND,INPUT); //Turn off LDR
    sleepl(); sleepl(); sleepl(); sleepl(); sleepl(); sleepl(); sleepl();
  }
  else
  {
    Serial.write("l1");
    Serial.flush();
    delay(2000);
    pinMode(ldrOUT,INPUT); //Turn off LDR
    pinMode(ldrGND,INPUT); //Turn off LDR
    sleepl(); sleepl();
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