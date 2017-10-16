import serial
from checar_conexao import *
from conexao_banco import *
from conexao_mqtt import *
import datetime
import time
import random
import json

#define o local de envio, a porta, o tempo e o topico
local = "localhost"
port_mqtt = 1883
timeout = 60
topico = "Tapajos-IoT"
qos = 1

#funcao para transformar os dados lidos de decimal para string
def binario_para_decimal(leitura):
    return str(float(leitura))

#comunicacaoSerial = serial.Serial('/dev/ttyACM0', 9600)

i = 1
while True:
    data = str(datetime.date.today())
    hora = str(datetime.datetime.now().time()).split(".")
    hora = str(hora[0])
    #value_bin = comunicacaoSerial.readline()
    #value = binario_para_decimal(value_bin)
    value =float("%.2f"%random.uniform(0.3,0.6))
    print("%d - corrente: %s A "%(i,value))
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
        print("Conexao com a internet estabelecida")
        while (num_de_documentos() > 0):
            #pega o dado que foi salvo no banco quando nao tinha conexao e envia
            print("Enviando para o brocker os dados armazenados no banco")
            conexao_mqtt(local,port_mqtt,timeout,topico,get_banco_local(),qos)
            #exclui os dados do banco
            excluir_dados_banco(get_banco_local())
        # envia o dado quando tem internet
        conexao_mqtt(local, port_mqtt,timeout,topico,doc,qos)
        print("Dado enviado para o broker")
    else:
        print("Sem conexao com a internet! Salvando dados no banco local")
        save_banco_local(doc)
    time.sleep(2)
    i +=1
