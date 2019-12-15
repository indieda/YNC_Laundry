void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}


void loop() {
  Serial.flush();
  Serial.write("z\n");
  delay(8000);
  }
