import time
import paho.mqtt.client as paho
import hashlib

broker="broker.hivemq.com"
filename="00005.jpg" #file to send
topic="cpd1995/surveillance"
qos=1
data_block_size=2000
fo=open(filename,"rb")

client= paho.Client("client-001")                           
client.on_publish=on_publish
client.puback_flag=False 
client.mid_value=None
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start()
start=time.time()
print("publishing ")
send_header(filename)