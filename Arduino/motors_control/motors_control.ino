#define SPEED_1      5
#define DIR_1        4

#define SPEED_2      6
#define DIR_2        7

void move_forward(int motor_speed) {
  digitalWrite(DIR_1, LOW);
  analogWrite(SPEED_1, motor_speed);
  digitalWrite(DIR_2, LOW);
  analogWrite(SPEED_2, motor_speed);
  Serial.println("Moving forward");
}

void stop_moving() {
  digitalWrite(DIR_1, LOW);
  analogWrite(SPEED_1, 0);
  digitalWrite(DIR_2, LOW);
  analogWrite(SPEED_2, 0);
  Serial.println("Stoping");
}

void setup() {
  Serial.begin(9600);
  for (int i = 4; i < 8; i++) {
    pinMode(i, OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    String a = Serial.readString();
    Serial.print(a);
    if (a == "stop\n"){
      stop_moving();
    }
    else if (a == "forward\n") {
      move_forward(100);
    }
  }
}