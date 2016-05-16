<img src="icon.png" align="right" width="200" height="200" />
# OnYourFace README
> An App to Recognize People

Upload a bunch of photos of you, your friends, your family or your favorite celebrity. Train the system, and recognize their other photos anytime, anywhere.

## Prerequisites

The environment set up process is designed keeping specific underlying operating system in mind. Will suggest to follow the setup process below on an Ubuntu machine preferably Ubuntu 14.04 or 16.04 on which the below process is tested and working OK.


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

* To avoid possible clashes with any existing development environment install [virtualenv](https://virtualenv.pypa.io/en/latest/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
```
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/.cache/pip
```

* Adding path variables to *.bashrc* for setting up virtualenv and virtualenvwrapper

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

* Setting up the virtual environment for deployment

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
  Setting up the build for installation
  ```
  cd ~/opencv
  mkdir build
  cd build
  cmake -D CMAKE_BUILD_TYPE=RELEASE \
	 -D CMAKE_INSTALL_PREFIX=/usr/local \
	  -D INSTALL_C_EXAMPLES=ON \
	   -D INSTALL_PYTHON_EXAMPLES=ON \
	    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	     -D BUILD_EXAMPLES=ON ..
  ```

## Articles
- ["How To Write A Readme"](http://jfhbrook.github.io/2011/11/09/readmes.html) - *Joshua Holbrook*
- ["How To Write A Great README"](https://robots.thoughtbot.com/how-to-write-a-great-readme) - *Caleb Thompson (thoughtbot)*
- ["Readme Driven Development"](http://tom.preston-werner.com/2010/08/23/readme-driven-development.html) - *Tom Preston-Werner*
- ["Top ten reasons why I won’t use your open source project"](https://changelog.com/top-ten-reasons-why-i-wont-use-your-open-source-project/) - *Adam Stacoviak*


## Contribute

Contributions are always welcome!
Please read the [contribution guidelines](contributing.md) first.


## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Matias Singers](http://mts.io) has waived all copyright and related or neighboring rights to this work.
