import serial
from checar_conexao import *
from conexao_banco import *
from conexao_mqtt import *
import datetime
import time
import random
import json

#define o local de envio, a porta, o tempo e o topico
local = '10.1.19.207'
port_mqtt = 1883
timeout = 60
topico = 'Tapajos-IoT'



comunicacaoSerial = serial.Serial('/dev/ttyACM1', 9600)

i = 1
while True:
	data = str(datetime.date.today())
	hora = str(datetime.datetime.now().time()).split('.')
	hora = str(hora[0])
	value_bin = comunicacaoSerial.readline()
	valor_lido = str(value_bin,'iso-8859-1')
	valor_lido = valor_lido.strip()
	

	try:
		type_sensor,model_sensor,name_sensor,value = valor_lido.split(',')
		#value = value.strip()
		#model_sensor = 'sct-13'
		#name_sensor = 'corrente01'
		#value = round(random.uniform(0.3,0.6),2)
		doc = {
   		"user": "yasminbraga",
		"local": "labic",
		"device": "raspberry pi",
		"hour": hora,
		"day": data,
		"type_sensor": type_sensor,
		"model_sensor": model_sensor,
		"name_sensor": name_sensor,
		"value": value }
		print('%d - '%i, name_sensor,' : %s A '%value)
		#print(doc)
		if checar_conexao() == True and checar_servidor(local,port_mqtt,timeout) == True:
			print("Conexao com a internet estabelecida")
			while (num_de_documentos() > 0):
				#pega o dado que foi salvo no banco quando nao tinha conexao e envia
				try:
					conexao_mqtt(topico,get_banco_local())
					#exclui os dados do banco
					excluir_dados_banco(get_banco_local())
					#envia o dado quando tem internet
					print("Enviando para o broker os dados armazenados no banco")
				except Exception as err:
					print(err)
					save_banco_local(get_banco_local())
			try:		
				conexao_mqtt(topico,doc)
				print("Dado enviado para o broker")
			except Exception as er:
				print(er)
		else:
			print("Sem conexao com a internet ou com o servidor! Salvando dados no banco local")
			save_banco_local(doc)
	except Exception as error:
		print('o erro ta aqui')
		print(error)
	i +=1

