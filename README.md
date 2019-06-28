# MSc_Dissertation

INSTRUCTIONS

To be ran on a Raspberry Pi Model 3b or greater.

wget https://bootstrap.pypa.io/get-pip.py

sudo python3 get-pip.py

sudo pip install opencv-contrib-python

sudo pip install imutils

sudo pip install face_recognition

python build_face_dataset.py --cascade haarcascade_frontalface_default.xml --output dataset/chris

python encode_faces.py --dataset dataset --encodings encodings.pickle

python prototype.py --encodings encodings.pickle
