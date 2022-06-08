/* Search and Rescue Robot Arduino code
 *  
 *  commands,
 *  1 forward, 2 left, 3 right, 4 backward
 *  
 *  author: ashraf minhaj
 *  mail  : ashraf_minhaj@yahoo.com
*/

#include<Servo.h>

// declare motor control pins
int left_motor_pin1  = 2;
int left_motor_pin2  = 3;
int right_motor_pin1 = 4;
int right_motor_pin2 = 5;

int arm_servo_pin   = 8;
int wrist_servo_pin = 7;
int claw_servo_pin  = 6;

String data;

Servo arm_servo;
Servo wrist_servo;
Servo claw_servo;

void setup() {
  // put your setup code here, to run once:
  pinMode(left_motor_pin1, OUTPUT);
  pinMode(left_motor_pin2, OUTPUT);

  pinMode(right_motor_pin1, OUTPUT);
  pinMode(right_motor_pin2, OUTPUT);

  arm_servo.attach(arm_servo_pin);
  wrist_servo.attach(wrist_servo_pin);
  claw_servo.attach(claw_servo_pin);
  
  Serial.begin(9600);
  delay(2000);

  // defalut pos of all servos
  arm_servo.write(180);
  wrist_servo.write(180);
}

void backward() {
  digitalWrite(left_motor_pin1, HIGH);
  digitalWrite(left_motor_pin2, LOW);

  digitalWrite(right_motor_pin1, HIGH);
  digitalWrite(right_motor_pin2, LOW);
}

void forward() {
  digitalWrite(left_motor_pin1, LOW);
  digitalWrite(left_motor_pin2, HIGH);

  digitalWrite(right_motor_pin1, LOW);
  digitalWrite(right_motor_pin2, HIGH);
}

void turn_left() {
  digitalWrite(left_motor_pin1, HIGH);
  digitalWrite(left_motor_pin2, LOW);

  digitalWrite(right_motor_pin1, LOW);
  digitalWrite(right_motor_pin2, HIGH);
}

void turn_right() {
  digitalWrite(left_motor_pin1, LOW);
  digitalWrite(left_motor_pin2, HIGH);

  digitalWrite(right_motor_pin1, HIGH);
  digitalWrite(right_motor_pin2, LOW);
}

void move_right(){
  digitalWrite(left_motor_pin1, LOW);
  digitalWrite(left_motor_pin2, HIGH);

  digitalWrite(right_motor_pin1, HIGH);
  digitalWrite(right_motor_pin2, LOW);
}

void stop(){
  digitalWrite(left_motor_pin1, LOW);
  digitalWrite(left_motor_pin2, LOW);

  digitalWrite(right_motor_pin1, LOW);
  digitalWrite(right_motor_pin2, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  int command_code;
  //  if(Serial.available()){}
    data = Serial.readStringUntil('\n');
    Serial.println("Received, " + data);
    command_code = data.toInt();
    Serial.println(command_code);
    
    if (command_code == 0){
      Serial.println("Stop");
      stop();
    }
    
    if (command_code == 1){
      Serial.println("Forward");
      forward();
    }

    if (command_code == 2){
      Serial.println("Turn left");
      turn_left();
    }

    if (command_code == 3){
      Serial.println("Turn Right");
      turn_right();
    }

    if (command_code == 4){
      Serial.println("Backward");
      backward();
    }

    if ((command_code >= 10) && (command_code <= 18)){
      int pos = map(command_code, 10, 18, 0, 180);
      arm_servo.write(pos);
      delay(100);
    }

	if ((command_code >= 20) && (command_code <= 28)){
      int pos = map(command_code, 20, 28, 0, 180);
      wrist_servo.write(pos);
      delay(100);
    }
    
    command_code = 0;
}
