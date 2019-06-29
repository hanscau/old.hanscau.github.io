#include <Ultrasonic.h>

const int pin = 5;  //Transistor Control Pin
Ultrasonic ultrasonic(7, 6); //Initialise Ultrasonic
int threshold = 0;  //Distance Threshold variable

void setup() {
  pinMode(A4, INPUT); //Set A4 as Analog Read
  pinMode(pin, OUTPUT); //Set pin 5 as output

  Serial.begin(9600); // Starts the serial communication
}

void loop() {
  int value = analogRead(A4); //Read from A4
  int distance = ultrasonic.distanceRead(); //Read from ultrasonic sensor

  threshold = map(value, 100, 1000, 5, 100); //Map threshold sensitivity

  //Print out all data
  Serial.print("Distance = ");
  Serial.print(distance);
  Serial.print(", Threshold = ");
  Serial.println(threshold);

  if (distance > threshold)
  {
    //Buzzer Off
    digitalWrite(pin, LOW);
  }
  else if (distance < threshold && distance > 0)
  {
    //Trigger Buzzer
    digitalWrite(pin, HIGH);
  }
  else  //when Ultrasonic sensor does not sense anything
  {
    //Buzzer Off
    digitalWrite(pin, LOW);
  }
}
