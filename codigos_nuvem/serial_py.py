import serial
from checar_conexao import *
from conexao_banco import *
from conexao_mqtt import *
import datetime
import time
import random
import json

#define o local de envio, a porta, o tempo e o topico
local = "10.1.19.201"
port_mqtt = 1883
timeout = 60
topico = "Tapajos-IoT"


def binario_para_decimal(leitura):
    return str(float(leitura))

comunicacaoSerial = serial.Serial('/dev/ttyACM0', 9600)

i = 1
while True:
    data = str(datetime.date.today())
    hora = str(datetime.datetime.now().time()).split(".")
    hora = str(hora[0])
    value_bin = comunicacaoSerial.readline()
    value = binario_para_decimal(value_bin)
    #value =float("%.2f"%random.uniform(0.3,0.6))
    print("%d - corrente: "%i,value," A")
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
        while (num_de_documentos() > 0):
            #pega o dado que foi salvo no banco quando nao tinha conexao e envia
            conexao_mqtt(local,port_mqtt,timeout,topico,get_banco_local())
            #print(type(get_banco_local()))
            #exclui os dados
            excluir_dados_banco(get_banco_local())
            # envia o dado quando tem internet
        #print(doc)
        conexao_mqtt(local, port_mqtt,timeout,topico,doc)
    else:
        save_banco_local(doc)
    time.sleep(2)
    i +=1
