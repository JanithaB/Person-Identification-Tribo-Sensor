#include "CyclicBuffer.h"

//defining for sensor1
const int analogPin1 = A0;
CyclicBuffer buffer1(10);
int dataList1[40];

//setup for serial comm
void setup(){
  Serial.begin(9600);
  delay(1000);
}

//main loop
void loop(){

  //reading sensor data from the analog inputs
  int sensorValue1 = analogRead(analogPin1);
  delay(10);
  Serial.println(sensorValue1);
//push data to the buffers
  buffer1.push(sensorValue1);
  
  //check whether the sensor data value reaching the limit to record the data
  if(sensorValue1>1020 && buffer1.isFull()){

//recording real time data to the datalists
    for(int i = 10;i<40; i++ ){
      dataList1[i]=analogRead(analogPin1);
      delay(10);
    }

//recording buffer data to the datalists
    for(int i = 0;i<10;i++){
      dataList1[i]=buffer1.get((i+buffer1.getHead())%buffer1.bufferSize());
    }
// Serial.print("\n DATA LIST \n");
//Serial print the datalists
    for(int i = 0;i<40;i++){
      Serial.print(dataList1[i]);
      Serial.print(" ");

    }
    Serial.print("\n");
    delay(1000);
  }

}
