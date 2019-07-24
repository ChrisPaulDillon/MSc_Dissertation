import random, string
import math
import time
import paho.mqtt.client as paho
import base64
import json
import argparse

broker="broker.hivemq.com"
filename="hi"#file to send
topic="cpd1995/surveillance"
qos=1
packet_size=2000

ap = argparse.ArgumentParser()
ap.add_argument('-e', '--encodings', default='encodings.pickle')
args = vars(ap.parse_args())

def publishEncodedImage():
    with open("00005.png", "rb") as image_file:
        encoded = base64.b64encode(image_file.read())
        byteArr = bytearray(image_file)
    end = packet_size
    start = 0
    length = len(encoded)
    picId = 1
    pos = 0
    no_of_packets = math.ceil(length/packet_size)

    client.publish(topic,encoded,qos)#publish
    
    while start <= len(encoded):
        data = {"data": encoded, "pic_id":picId, "pos": pos, "size": no_of_packets}
        print("Pos:",pos ,"size:", no_of_packets, "data: ", encoded)
       #client.publish(topic,byteArr,qos)#publish 
        end += packet_size
        start += packet_size
        pos = pos +1
    
client= paho.Client("client-001")                           
client.puback_flag=False 
client.mid_value=None
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start()
start=time.time()
print("publishing ")
publishEncodedImage()