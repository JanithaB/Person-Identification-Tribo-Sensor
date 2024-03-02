#include "CyclicBuffer.h"

//defining for sensor1
const int analogPin1 = A0;
CyclicBuffer buffer1(100);
 

const int analogPin2 = A1;
CyclicBuffer buffer2(100);
int dataList2[200];

const int analogPin3 = A2;
CyclicBuffer buffer3(100);
int dataList3[200];

const int analogPin4 = A3;
CyclicBuffer buffer4(100);
int dataList4[200];

const int analogPin5 = A4;
CyclicBuffer buffer5(100);
int dataList5[200];

const int analogPin6 = A5;
CyclicBuffer buffer6(100);
int dataList6[200];


//setup for serial comm
void setup(){
  Serial.begin(9600);
  pinMode(10,OUTPUT);
  delay(1000);
}

//main loop
void loop(){

  //reading sensor data from the analog inputs
  int sensorValue1 = analogRead(analogPin1);
  delay(10);
  int sensorValue2 = analogRead(analogPin2);
  delay(10);
  int sensorValue3 = analogRead(analogPin3);
  delay(10);
  int sensorValue4 = analogRead(analogPin4);
  delay(10);
  int sensorValue5 = analogRead(analogPin5);
  delay(10);
  int sensorValue6 = analogRead(analogPin6);
  delay(10);

//push data to the buffers
  buffer1.push(sensorValue1);
  buffer2.push(sensorValue2);
  buffer3.push(sensorValue3);
  buffer4.push(sensorValue4);
  buffer5.push(sensorValue5);
  buffer6.push(sensorValue6);
  
  //check whether the sensor data value reaching the limit to record the data
  if((sensorValue1>50 || sensorValue2>50) &&  buffer1.isFull()){
digitalWrite(10,HIGH);
//recording real time data to the datalists
    for(int i = 100;i<200; i++ ){
      dataList1[i]=analogRead(analogPin1);
      delay(10);
      dataList2[i]=analogRead(analogPin2);
      delay(10);
      dataList3[i]=analogRead(analogPin3);
      delay(10);
      dataList4[i]=analogRead(analogPin4);
      delay(10);
      dataList5[i]=analogRead(analogPin5);
      delay(10);
      dataList6[i]=analogRead(analogPin6);
      delay(10);
    }
digitalWrite(10,LOW);
//recording buffer data to the datalists
    for(int i = 0;i<100;i++){
      dataList1[i]=buffer1.get(i);
      dataList2[i]=buffer2.get(i);
      dataList3[i]=buffer3.get(i);
      dataList4[i]=buffer4.get(i);
      dataList5[i]=buffer5.get(i);
      dataList6[i]=buffer6.get(i);

      // dataList1[i]=buffer1.get((i+buffer1.getHead())%buffer1.bufferSize());
      // dataList2[i]=buffer2.get((i+buffer2.getHead())%buffer2.bufferSize());
      // dataList3[i]=buffer3.get((i+buffer3.getHead())%buffer3.bufferSize());
      // dataList4[i]=buffer4.get((i+buffer4.getHead())%buffer4.bufferSize());
      // dataList5[i]=buffer5.get((i+buffer5.getHead())%buffer5.bufferSize());
      // dataList6[i]=buffer6.get((i+buffer6.getHead())%buffer6.bufferSize());
    }

//Serial print the datalists
    for(int i = 0;i<200;i++){
      Serial.print(dataList1[i]);
      Serial.print(" ");
      Serial.print(dataList2[i]);
      Serial.print(" ");
      Serial.print(dataList3[i]);
      Serial.print(" ");
      Serial.print(dataList4[i]);
      Serial.print(" ");
      Serial.print(dataList5[i]);
      Serial.print(" ");
      Serial.print(dataList6[i]);
      Serial.print("\n");
    }
    buffer1.clear();
    buffer2.clear();
    buffer3.clear();
    buffer4.clear();
    buffer5.clear();
    buffer6.clear();
  }
}
