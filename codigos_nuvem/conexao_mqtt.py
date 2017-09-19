import paho.mqtt.client as mqtt
import json

client = mqtt.Client()
	
def conexao_mqtt(local, port,timeout,topico,doc):
	try:
		client.connect(local,port,timeout)
		client.publish(topico, json.dumps(doc))
	except Exception as error:
		print(error)





