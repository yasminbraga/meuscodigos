import paho.mqtt.client as mqtt
import json
from conexao_banco import *

client = mqtt.Client()

def checar_servidor(local, port,timeout):
	try:
		client.connect(local,port,timeout)
		return True
	except Exception as error:
		print(error)
		return False

def conexao_mqtt(topico,doc):
    try:
        client.publish(topico, json.dumps(doc))
    except Exception as error:
        print(error)
        
