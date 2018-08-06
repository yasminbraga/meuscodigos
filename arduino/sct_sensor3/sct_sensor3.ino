#include "EmonLib.h"
#include <SPI.h>
#include "DS1307.h"

DS1307 rtc (A4,A5);

EnergyMonitor emon1;

int i=1;

int pino_sct = A1;


void setup() {
  rtc.halt(false);
  //rtc.setDOW(TUESDAY);
  //rtc.setTime(10,28,0);
  //rtc.setDate(24,04,2018);

  rtc.setSQWRate(SQW_RATE_1);
  rtc.enableSQW(true);

  Serial.begin(9600);
  emon1.current(pino_sct,53);
  
}

void loop() {
 
  Serial.print(i);
  Serial.print(" ");
  Serial.print(rtc.getTimeStr());
  Serial.print(" ");

  double Irms = emon1.calcIrms(1480);
  Serial.print(Irms*1.358 - 0.1493);
  //Serial.print(" A");
  Serial.print("\n");
  delay(1000);
  i++;
}
