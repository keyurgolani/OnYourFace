<img src="icon.png" align="right" width="200" height="200" />
# OnYourFace README
> An App to Recognize People

Upload a bunch of photos of you, your friends, your family or your favorite celebrity. Train the system, and recognize their other photos anytime, anywhere.


## Prerequisites

The environment set up process is designed keeping specific underlying operating system in mind. Will suggest to follow the setup process below on an Ubuntu machine preferably *Ubuntu 14.04* or *Ubuntu 16.04* on which the below process is tested and working OK.


## Getting Started - Setting up the Environment
* **Making sure that the base OS has all the latest packages.**
```
sudo apt-get update
sudo apt-get upgrade
```

* **Installing developer tools for linux system.**
```
sudo apt-get install build-essential cmake git pkg-config
```

* **Installing supporting libraries for OpenCV**

  Installing support to load various types of Images
  ```
  sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
  ```
  Installing support for displaying images on screenshot
  ```
  sudo apt-get install libgtk2.0-dev
  ```
  Installing support for image and video processing
  ```
  sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
  ```
  Installing image processing routines optimization libraries
  ```
  sudo apt-get install libatlas-base-dev gfortran
  ```

* **Installing *pip*, a popular python package manager**
```
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
```

* **To avoid possible clashes with any existing development environment install [virtualenv](https://virtualenv.pypa.io/en/latest/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)**
```
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/.cache/pip
```

* **Adding path variables to *.bashrc* for setting up virtualenv and virtualenvwrapper**

  Add the following lines to *~/.bashrc* file using simple text editors of choice
  ```
  # virtualenv and virtualenvwrapper
  export WORKON_HOME=$HOME/.virtualenvs
  source /usr/local/bin/virtualenvwrapper.sh
  ```
  Execute below command to reset the *~/.bashrc* file and take effect into bash terminal
  ```
  source ~/.bashrc
  ```
  Execute below command to create a new virtual environment
  ```
  mkvirtualenv opencv
  ```

* **Setting up the virtual environment for deployment**

  Installing python development tools
  ```
  sudo apt-get install python2.7-dev
  ```
  Installing numpy for processing images as a multi-dimensional arrays.
  ```
  sudo pip install numpy
  ```
  Downloading OpenCV Supporting Modules Source
  ```
  cd ~
  git clone https://github.com/Itseez/opencv.git
  cd opencv
  git checkout 3.0.0
  ```
  Downloading OpenCV Supporting Modules Source
  ```
  cd ~
  git clone https://github.com/Itseez/opencv_contrib.git
  cd opencv_contrib
  git checkout 3.0.0
  ```
  Setting up the build for compilation
  ```
  cd ~/opencv
  mkdir build
  cd build
  cmake -D CMAKE_BUILD_TYPE=RELEASE \ -D CMAKE_INSTALL_PREFIX=/usr/local \ -D INSTALL_C_EXAMPLES=ON \ -D INSTALL_PYTHON_EXAMPLES=ON \ -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \ -D BUILD_EXAMPLES=ON ..
  ```
  Compiling the code of OpenCV and Supporting Modules
  ```
  make -j5
  ```
  Installing and setting up OpenCV and the Modules
  ```
  sudo make install
  sudo ldconfig
  ```
  Configuring the virtual environment with installed OpenCV packages
  ```
  cd ~/.virtualenvs/cv/lib/python2.7/site-packages/
  ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so
  ```
  Verifying successful installation of the environment
  ```
  workon opencv
  python
  >>> import cv2
  >>> cv2.__version__
  '3.0.0'
  ```

* **Installing Flask for Web Application Deployment**
```
sudo pip install flask
```

* **Installing Pilliw for Image saving and loading**
```
sudo pip install Pillow
```

* **Installing JSON parsing**
```
sudo pip install simplejson
```

* **Installing MySQL for Information Storage**
```
sudo apt-get install mysql-server
```


## Setting up the application
* **Setting up the database**

  Login as root user
  ```
  mysql -u root -p
  <root account password that you set while installing mysql>
  ```
  Create a new database
  ```
  create database LabelInfo
  use LabelInfo
  ```
  Create table for the label information
  ```
  CREATE TABLE `LabelInfo`.`tbl_details` (`label_id` BIGINT NOT NULL AUTO_INCREMENT, `first_name` VARCHAR(45) NULL, `last_name` VARCHAR(45) NULL, `location` VARCHAR(45) NULL, `birthdate` DATE NULL, PRIMARY KEY (`label_id`));
  ```

* **Giving our code the information about mysql connectivity**

  Open Terminal and navigate to Home directory
  ```
  cd ~
  ```
  Download the project from github repository
  ```
  git clone https://github.com/keyurgolani/OnYourFace.git
  ```
  Find app.py into the project
  ```
  cd ~/OnYourFace/OnYourFace/
  ```
  Open app.py in any terminal *example gedit*
  ```
  gedit ~/OnYourFace/OnYourFace/app.py
  ```
  Change the mysql database user information to your instance information on lines 15 through 18
  ```
  app.config['MYSQL_DATABASE_USER'] = 'root'
  app.config['MYSQL_DATABASE_PASSWORD'] = '<The password you set for root user while installing mysql>'
  app.config['MYSQL_DATABASE_DB'] = 'LabelInfo'
  app.config['MYSQL_DATABASE_HOST'] = 'localhost'
  ```

* **Starting the Application**
```
cd ~/OnYourFace/
python ~/OnYourFace/runserver.py
```


## Using the Application
* **Accessing the Application**
  - The application, with the default configurations, should be up and running on localhost at 2016 port.
  - Open your browser and access the application with following URL in address bar.
  ```
  https://localhost:2016/
  ```
* **Training the system**
  - Go to **Upload** tab from the header of the application.
  - Fill in the information for the person you want to upload photos of.
  - Select multiple photos of the person in which the person's frontal face is visible. **The more photos the better. But upload the right photos.**
  - Click the *upload* button.
  - Repeat this step for each separate individual you want to train the application for.
  - At the end, go to the **Train** tab on the header, click *Train*, sit back and relax for a while.

* **Identifying a person**
  - After training the application with several photos, you will automatically be redirected to the recognize page. If not, you can access it through **Recognize** tab on the header.
  - Select the photo to be recognized and click *Recognize* button at the bottom and let the application work its magic.

Have a little fun with the application.
Suggest more functionalities. I will try to integrate more and more as suggestions come in.
**Contributions are always welcome. Let's make it big.**

## Foot-note:
If you try to recognize a person that the application has not been trained, it will try to find the closest feature match from the people it has been trained with.

## Future Plans:
- Integrate video capabilities for training and recognizing the face.
- Integrating object recognition feature.
- Integrating OCR facility.
- Integrating nudity recognition.
- and suggested features of course.
