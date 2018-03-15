#include "EmonLib.h" //Define a biblioteca para o sensor de corrente

//Bloco para print 
String valoresCorrente;
String valoresTensao;
char const* infoCorrente = "corrente,sct-013,corrente-00,";
char const* infoTensao = "tensao,p8,tensao-01,";

//variaveis para funcionamento do sensor
int sensorTensao = A0;
float valorCorrente = 0;
float valorTensao = 0;
int amostragem = 1000;
float somaTotal = 0;
float mediaTotal = 0;
float valorFinal = 0;
EnergyMonitor emon1;
int pino_sct = A1;

void setup() {
  emon1.current(pino_sct,55);
  analogReference(DEFAULT);
  pinMode(sensorTensao,INPUT);
  Serial.begin(9600); 
 }

void loop() {
  //recebe o valor de corrente
  double Irms = emon1.calcIrms(1480);
  
  float somaTotal = 0;
  float mediaTotal = 0;
  float valorFinal = 0;
  //recebe 1000 valores de tensao e tira a media
  for(int i = 0; i < amostragem; i++){
    valorTensao = analogRead(sensorTensao);
    mediaTotal = mediaTotal + valorTensao;
  }
  mediaTotal = mediaTotal/amostragem;
  
//bloco referente a tensao de 127V
  if ((mediaTotal >100) & (mediaTotal <483)){
    valorFinal = ((mediaTotal*5)/1023)*64.3;
  }
//bloco referente a tensao de 220V
  if ((mediaTotal>665) & (mediaTotal<1023)){
    valorFinal = ((mediaTotal*5)/1023)*56.5;
  }
  //valor de corrente referente ao parametro de validacao
  Irms = Irms*1.138-0.1571;
  
  valoresCorrente = infoCorrente + String(Irms);
  valoresTensao = infoTensao + String(valorFinal);
  
  Serial.println(valoresCorrente);
  //Serial.print("\n");
  Serial.println(valoresTensao);
  //Serial.print("\n");
  
  delay(1000);
 }
  
  


