import paho.mqtt.client as mqtt
import json

client = mqtt.Client()
	
def conexao_mqtt(local, port,timeout,topico,doc,qos):
    try:
        client.connect(local,port,timeout)
        client.publish(topico, json.dumps(doc),qos)
    except Exception as error:
        print(error)





