int incomingByte = 0;

void show_one(){
  Serial.println("You entered 0");
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    incomingByte = Serial.read();

    if (incomingByte == '0') {
      show_one();
    }
    else if (incomingByte == '1') {
      Serial.println("You entered 1");
    }
    else if (incomingByte == '2') {
      Serial.println("You entered 2");
    }
    else if (incomingByte == '3') {
      Serial.println("You entered 3");
    }
  }
}
