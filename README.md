<img src="icon.png" align="right" />
# OnYourFace README
> An App to Recognize People

Upload a bunch of photos of you, your friends, your family or your favorite celebrity. Train the system, and recognize their other photos anytime, anywhere.

## Prerequisites

- The environment set up process is designed keeping specific underlying operating system in mind. Will suggest to follow the setup process below on an Ubuntu machine preferably Ubuntu 14.04 or 16.04 on which the below process is tested and working OK.


## Getting Started - Setting up the Environment
1. Making sure that the base OS has all the latest packages.
```
sudo apt-get update
sudo apt-get upgrade
```

2. Installing developer tools for linux system.
```
sudo apt-get install build-essential cmake git pkg-config
```

3. Installing supporting libraries for OpenCV
- Installing support to load various types of Images
```
sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
```
- Installing support for displaying images on screenshot
```
sudo apt-get install libgtk2.0-dev
```
- Installing support for image and video processing
```
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
```
- Installing image processing routines optimization libraries
```
sudo apt-get install libatlas-base-dev gfortran
```

4. Installing **pip**, a popular python package manager
```
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
```

5. 
- [sindresorhus/pageres](https://github.com/sindresorhus/pageres) - Project logo. Clear description of what the project does. Build badges. Demo screenshot. Simple install and usage sections. Includes an examples section with common uses.
- [petkaantonov/bluebird](https://github.com/petkaantonov/bluebird) - Build badges. Clear description of what the project does. TOC for easy navigation. Project logo. Extensive explanations and examples.
- [jakubroztocil/httpie](https://github.com/jkbrzt/httpie) - Description of what the project does. Demo screenshots. Project logo. TOC for easy navigation. Build badges. Quick and simple installation and usage sections. Includes an examples section.
- [karan/joe](https://github.com/karan/joe) - Project logo. Clear description of what the project does. GIF demo. Easy install and usage sections.
- [aimeos/aimeos-typo3](https://github.com/aimeos/aimeos-typo3) - Project logo. Clear description of what the project does. Demo screenshot. TOC for easy navigation. Easy installation and setup sections with screenshots. Links for further reading.
- [rstacruz/hicat](https://github.com/rstacruz/hicat) - GIF demo. Easy installation and setup sections with screenshots. Build badges. Great examples of use cases.
- [skywinder/github-changelog-generator](https://github.com/skywinder/github-changelog-generator) - TOC for easy navigation. Concise project description. Installation and usage sections. Output example. Great feature overview. List of alternatives. FAQ.
- [shama/gaze](https://github.com/shama/gaze) - Project logo. Concise description. Feature list. Usage section. FAQ. Great API documentation. Release history.
- [node-chat](https://github.com/IgorAntun/node-chat) - Project screenshot. Informative badges. Clear description. Easy installation/use instructions. Live demo.
- [b4b4r07/dotfiles](https://github.com/b4b4r07/dotfiles) - Testing my dotfiles repo on OS X to get my work environment ready in just a few moments. #VIM + #ZSH + #TMUX = Best Developer Environment.

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
