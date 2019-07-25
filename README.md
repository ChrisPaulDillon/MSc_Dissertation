# MSc_Dissertation

**Version 1.3 **

This is the Raspberry Pi related code for a face recognition based surveillance system.
The idea behind the system is to provide a secure way of identifying possible threats and sending
a push notification to all connected devices. 

## INSTRUCTIONS

To be ran on a Raspberry Pi Model 3b or greater and Python 3.5 or greater.

wget https://bootstrap.pypa.io/get-pip.py

sudo python3 get-pip.py

### Downloading OpenCV4

wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0.zip

wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip

unzip opencv.zip

unzip opencv_contrib.zip

mv opencv-4.0.0 opencv

mv opencv_contrib-4.0.0 opencv_contrib


** I recommend downloading these files while doing the next step to save time **

### OpenCv Prerequisites Libraries

sudo apt-get install build-essential cmake unzip pkg-config

sudo apt-get install libjpeg-dev libpng-dev libtiff-dev

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

sudo apt-get install libxvidcore-dev libx264-dev

sudo apt-get install libgtk-3-dev

sudo apt-get install libcanberra-gtk*

sudo apt-get install libatlas-base-dev gfortran

### Configuring Virtual Environment for OpenCV4

sudo pip install virtualenv virtualenvwrapper

sudo rm -rf ~/get-pip.py ~/.cache/pip

echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.profile

echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile

echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.profile

echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile

source ~/.profile

mkvirtualenv cv -p python3

workon cv

pip install numpy

### CMake & Compiling OpenCV4

cd ~/opencv

mkdir build

cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D ENABLE_NEON=ON \
    -D ENABLE_VFPV3=ON \
    -D BUILD_TESTS=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=OFF ..

### Increasing Swap Size Temporarily

sudo nano /etc/dphys-swapfile

Change value CONF_SWAPSIZE=100 to CONF_SWAPSIZE=2048

sudo /etc/init.d/dphys-swapfile stop

sudo /etc/init.d/dphys-swapfile start

make -j4

sudo make install

sudo ldconfig

---
### Additional Libraries required

-sudo pip install imutils

-sudo pip install face_recognition


