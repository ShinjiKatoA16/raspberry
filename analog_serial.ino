// get Analog data and send it via USB-serial
// in order to view the value in IDE, click Serial Monitor

const int SENSOR = 0 ;
int val = 0;

void setup() {
  Serial.begin(38400);
}

void loop() {
  val = analogRead(SENSOR) ;
  
  Serial.println(val, HEX) ;
  delay(500) ;
}
