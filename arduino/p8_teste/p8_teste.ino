#define R1 220000.0
#define R2 10000.0
#define SAMPLES 5
float acum  = 0;
int analog0 = 0;
int loops   = 0;
float v1    = 0;

void calc(){
  analog0 = analogRead(0);
  v1 = (5.0 * analog0)/1024.0;
  Serial.print("Valor da amostragem ");
  Serial.print(loops);
  Serial.print(": ");
  Serial.println(v1);
  
  if (v1 < 1){
    return;
  }
  acum += v1/(R2/(R2+R1));
  
  loops++;
  
  if (loops >4){
    loops = 0;
    float result = acum/SAMPLES;
    Serial.print("V=");
    Serial.println(result);
  }
  delay(200);
}
void setup() {
  pinMode(0,INPUT);
  Serial.begin(9600);
  Serial.println("Iniciando");
}

void loop() {
  calc();

}
