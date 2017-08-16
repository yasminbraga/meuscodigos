import serial
from checar_conexao import *
from conexao_banco import *
from conexao_mqtt import *
import datetime
import time 

local = "10.1.19.35"
port_mqtt = 1883
timeout = 60
topico = "Tapajos-IoT"
data = str(datetime.date.today())
hora = str(datetime.datetime.now().time()).split(".")
hora = str(hora[0])

def binario_para_decimal(leitura):
    return str(float(leitura))

#comunicacaoSerial = serial.Serial('/dev/ttyACM0', 9600)

while True:
	#value_bin = comunicacaoSerial.readline()
	#value = binario_para_decimal(value_bin)
	value = 0.49
	print("corrente: ",value," A")

	doc = {
   		"user": "yasmin",
		"local": "labic",
		"device": "raspberry pi",
		"hour": hora,
		"day": data,
		"type_sensor": "corrente",
		"model_sensor": "SCT-013",
		"value": value }
	
	if checar_conexao() == True:
		# pega o dado que foi salvo e envia
		function
		# envia o dado quando tem internet
		conexao_mqtt(local, port_mqtt,timeout,topico,doc)
		
	else:
		save_banco_local(doc)
	time.sleep(2)
