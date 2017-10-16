import paho.mqtt.client as mqtt
import time

broker = "localhost"
port = 1883

def on_log(client, userdata, level, buf):
    print(buf)
def on_connect(client, userdata,flags,rc):
    if rc ==0:
        client.connected_flag = True
        print("connected ok")
    else:
        print("Bad connection Returned code = ", rc)
        client.loop_stop()
def on_disconnect(client,userdata,mid):
    print("client disconnect ok")
def on_publish(client,userdata,mid):
    print("In on_pub callback mid = ", mid)
    
mqtt.Client.connected_flag = False
client = mqtt.Client("python1")
client.on_log = on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.connect(broker,port)
client.loop_start()
while not client.connected_flag:
    print("In wait loop")
    time.sleep(1)
time.sleep(3)
print("publishing")
ret = client.publish("house", "test 2", 2)
print("published return = ", ret)
time.sleep(3)
        