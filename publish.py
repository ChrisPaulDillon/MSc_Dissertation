import random, string
import math
import time
import paho.mqtt.client as paho
import base64
import json
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--img", default="dataset/00005.png",
    help="path to serialized db of facial encodings")
args = vars(ap.parse_args())

broker="broker.hivemq.com"
filename=args["img"]
topic="cpd1995/surveillance"
qos=2
packet_size=2000

def publishEncodedImage():
    with open(filename, "rb") as image_file:
        encoded = base64.b64encode(image_file.read())
        byteArr = bytearray(image_file)
    end = packet_size
    start = 0
    length = len(encoded)
    picId = 1
    pos = 0
    no_of_packets = math.ceil(length/packet_size)

    client.publish(topic,encoded,qos)
    
    while start <= len(encoded):
        data = {"data": encoded, "pic_id":picId, "pos": pos, "size": no_of_packets}
        print("Pos:",pos ,"size:", no_of_packets, "data: ", encoded)
        end += packet_size
        start += packet_size
        pos = pos +1
    
client= paho.Client("client-001")                           
client.puback_flag=False 
client.mid_value=None
print("Connecting To Broker ",broker)
client.connect(broker)
client.loop_start()
start=time.time()
print("Publishing ")
publishEncodedImage()
