# Envio de dados do sensor de corrente para a nuvem

## Introdução


## Hardware
O Hardware utilizado constitui-se de tecnologias Open Source e dos componentes eletrônicos listados a seguir

* Arduino Uno
* Raspberry Pi 3 Model B
* 2 resistores de 10KΩ (para o divisor de tensão)
* 1 resistor de 33Ω (para o resistor de carga)
* 1 capacitor de 10µF
* Sensor Sct-013 de 100 A

![sct_arduino](docs/sct_arduino.png)

## Integração Arduino e Raspberry
A integração entre Arduino e Raspberry Pi é feita com comunicação serial. Isso é feito ao conectar o cabo USB do Arduino a uma das portas do Raspberry Pi (no caso foi usado a primeira).

Antes da conexao, no prompt de comando do Raspberry digite o seguinte:
```
ls /dev/tty*
```
Depois conecte o cabo e novamente digite o codigo. Será acrescentado uma porta na lista que é a porta em que o Arduino esta conectado (normalmente "/dev/ttyACM0").

Istale o Pyserial

## Software Arduino

## Software Raspberry
