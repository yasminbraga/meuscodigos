#include "EmonLib.h" //Define a biblioteca para o sensor de corrente

//Bloco para print de informacoes
String valoresCorrente;
String valoresTensao;
char const* infoCorrente = "corrente,sct-013,corrente-00,";
char const* infoTensao = "tensao,p8,tensao-01,";

//variaveis para funcionamento do sensor de tensao
int pinoTensao = A0;
float valorTensao = 0;
float media = 0;
float tensao = 0;
//variaveis para funcionamento do sensor de corrente
EnergyMonitor emon1;
int pinoCorrente = A1;

void setup() {
  emon1.current(pinoCorrente,55);
  analogReference(DEFAULT);
  pinMode(pinoTensao,INPUT);
  Serial.begin(9600); 
 }

void loop() {
  //recebe o valor de corrente
  double Irms = emon1.calcIrms(1480);

  //recebe o valor de tensao
  media = 0;
  for(int i = 0;i<10000;i++){
    valorTensao = analogRead(pinoTensao);
    media = valorTensao + media;
  }
  
  tensao = media/10000;
  //Serial.println(tensao);
  //bloco referente a tensao de 127 V
  if (tensao>70 && tensao <854){
    tensao = tensao*0.148;
  }
  //bloco referente a tensao de 220 V
  else if(tensao > 861){
    tensao = tensao*0.252;
  }
  else{
    tensao = 0;
  }

  //valor de corrente referente ao parametro de validacao
  Irms = Irms*1.138-0.1571;
  
  //uniao de informacoes referentes aos sensores + o dado recebido
  valoresCorrente = infoCorrente + String(Irms);
  valoresTensao = infoTensao + String(tensao);
  
  Serial.println(valoresCorrente);
  Serial.println(valoresTensao);
  
  
  delay(1000);
 }
