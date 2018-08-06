#include "EmonLib.h"
#include <SPI.h>
#include "DS1307.h"

DS1307 rtc (A4,A5);

EnergyMonitor emon1;

int i=1;

int pino_sct = A1;


void setup() {
  rtc.halt(false);
  rtc.setDOW(WEDNESDAY);
  rtc.setTime(12,10,0);
  //rtc.setDate(08,02,2018);

  rtc.setSQWRate(SQW_RATE_1);
  rtc.enableSQW(true);

  Serial.begin(9600);
  emon1.current(pino_sct,55);
  
}

void loop() {
 /*
  Serial.print(i);
  Serial.print(" ");
  Serial.print(rtc.getTimeStr());
  Serial.print(" ");
*/
  double Irms = emon1.calcIrms(1480);
  //y = 0,878x + 0,1379 - reta obtida 
  Serial.print(Irms*1.138-0.1571);
  Serial.print("\n");
  Serial.print(Irms);
  Serial.print(" A");
  Serial.print("\n");
  delay(1000);
  i++;
}
