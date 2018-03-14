int pinotensao = A0;
float valortensao = 0;
float media = 0;
float tensao = 0;
void setup() {
  pinMode(pinotensao,INPUT);
  Serial.begin(9600);

}

void loop() {
  media = 0;
  for(int i = 0;i<10000;i++){
    valortensao = analogRead(pinotensao);
    media = valortensao +media;
  }
  
  tensao = media/10000;
  //Serial.println(tensao);
  if (tensao>70 && tensao <854){
    tensao = tensao*0.148;
  }
  else if(tensao > 861){
    tensao = tensao*0.252;
  }
  else{
    tensao = 0;
  }
  //valortensao = analogRead(pinotensao)*0.146;
  //valortensao = analogRead(pinotensao);
  Serial.println(tensao);
  Serial.print("\n");
  delay(1000);


}
