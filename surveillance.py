from imutils.video import VideoStream
from imutils.io import TempFile
from datetime import datetime
from datetime import date
import numpy as np
import argparse
import imutils
import signal
import time
import cv2
import sys
import pickle
import face_recognition
import os
import subprocess

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="dataset/",
    help="path to output image")
ap.add_argument("-y", "--display", type=int, default=1,
    help="whether or not to display output frame to screen")
args = vars(ap.parse_args())

print("[INFO] loading encodings...")
data = pickle.loads('encodings', "rb").read())

#Initialize the video stream and allow the camera sensor to warmup
print("[INFO] warming up camera...")
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
total = 0

#Loop over the frames of the stream
while True:
    #Grab the frame from the threaded video stream
    frame = vs.read()
    orig = frame.copy()
    #Convert the input frame from BGR to RGB then resize it to have a width of 750px (to speedup processing)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb = imutils.resize(frame, width=750)
    r = frame.shape[1] / float(rgb.shape[1])

    #Detect the (x, y)-coordinates of the bounding boxes
    #Corresponding to each face in the input frame, then compute the facial embeddings for each face
    boxes = face_recognition.face_locations(rgb,
        model=hog)
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    #loop over the facial embeddings
    for encoding in encodings:
        #Attempt to match each face in the input image to our known encodings
        matches = face_recognition.compare_faces(data["encodings"],
            encoding)
        name = "Unknown"

        #Check if match is found
        if True in matches:
            # find the indexes of all matched faces then initialize a
            # dictionary to count the total number of times each face
            # was matched
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            # determine the recognized face with the largest number
            # of votes (note: in the event of an unlikely tie Python
            # will select first entry in the dictionary)
            name = max(counts, key=counts.get)
                  
        #Update the list of names
        names.append(name)

    #Loop over the recognized faces
    for ((top, right, bottom, left), name) in zip(boxes, names):
        # rescale the face coordinates
        top = int(top * r)
        right = int(right * r)
        bottom = int(bottom * r)
        left = int(left * r)

        #Draw predicted name in frame
        cv2.rectangle(frame, (left, top), (right, bottom),
            (0, 255, 0), 2)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
            0.75, (0, 255, 0), 2)
 	print (name, " Detected!")
        if name == 'Unknown':
            print("[INFO] Unknown face detected! Taking screenshot!")
            dateTime = datetime.now()
            p = os.path.sep.join([args["output"], "{}.jpg".format(
            str(dateTime))])
            cv2.imwrite(p, orig)
            subprocess.call(["python3", "/home/pi/Diss/publish.py", "--img",
                             "/home/pi/Diss/dataset/" + str(dateTime) + '.jpg'])
            time.sleep(10.0)
            
    #Check to see if we are supposed to display the output frame to the screen
    if args["display"] > 0:
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

#Cleanup
cv2.destroyAllWindows()
vs.stop()
