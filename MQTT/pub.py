import random, string
import math
import time
import paho.mqtt.client as paho
import base64
import json

packet_size=64000
broker="broker.hivemq.com"
filename="00005.jpg" #file to send
topic="cpd1995/surveillance"
qos=2

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

def convertImageToBase64():
    with open(filename, "rb") as image_file:
        encoded = base64.b64encode(image_file.read())
    return encoded

def publishEncodedImage(encoded):
    client.publish(topic,encoded,qos)#publish
    
def testPub():
    client.publish(topic,"Pls work",qos)#publish
    
client= paho.Client("client-001")
client.on_publish = on_publish  
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start()
start=time.time()
print("publishing ")
#publishEncodedImage(convertImageToBase64())
testPub()
