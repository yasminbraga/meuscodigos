import serial
from checar_conexao import *
from conexao_banco import *
from conexao_mqtt import *
import datetime
import time 

local = "10.1.19.110"
port_mqtt = 1883
timeout = 60
topico = "Tapajos-IoT"

def binario_para_decimal(leitura):
    return str(float(leitura))

comunicacaoSerial = serial.Serial('/dev/ttyACM0', 9600)

while 1:
	value_bin = comunicacaoSerial.readline()
	value = binario_para_decimal(value_bin)
	print("corrente: ",value," A")

	doc = {
   		user: "yasmin",
		local: "laboratório",
		device: "raspberry pi",
		hour: "15:31:22",
		day: "10-07-2017"
		type_sensor: "corrente",
		model_sensor: "SCT-013",
		value: value }
	
	if checar_conexao() == True:
		conexao_mqtt(local, port_mqtt,timeout,topico)
	else:
		conexao_local_banco(doc)

