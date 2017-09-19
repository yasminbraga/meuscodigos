import paho.mqtt.client as mqtt

client = mqtt.Client()
	
def conexao_mqtt(local, port,timeout, topico, doc):
	try:
		client.connect(local,port,timeout)
		client.publish(topico, doc)
	except Exception as error:
		print(error)




