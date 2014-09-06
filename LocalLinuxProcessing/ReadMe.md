Local Linux processing of G+ Hangouts
---
There are several things you need to setup before this will work.
##### You need the following packages and their dependencies:
* ffmpeg - 5:0.7.15-dmo1 audio/video encoder, streaming server & audio/video file converter
* sox - 14.3.1-1+b1 Swiss army knife of sound processing
* youtube-dl - http://rg3.github.com/youtube-dl/
* python - 2.6.6 or better is required by youtube-dl and fabric

##### Python packages that are needed:
* setuptools
* pip
* fabric

##### Getting setuptools
1. Download the version for your version of Python (python --version)  
    `wget https://pypi.python.org/packages/2.6/s/setuptools/setuptools-0.6c11-py2.6.egg#md5=bfa92100bd772d5a213eedd356d64086`
2. run the setup script as root  
    `sudo sh setuptools-0.6c11-py2.6.egg`

##### Install PIP
1. Download the install script  
    `wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py`
2. Run the python as root  
    `sudo python get-pip.py`

##### Install Fabric  
pip is great becuase it will automatically install the dependencies  
`sudo pip install fabric`


##### Running the command  
1. Go to the Youtube page for the podcast  
    You should be at a URL similar to this one for podcast 81  
    https://www.youtube.com/watch?v=NyBNdQHSPUM  
    Be ready to copy the end of the URL after the v= to past in when the script prompts you.  
2. In a terminal window cd to the directory this document and the processPodcast.sh script are located.  
3. run the script  
    `./processPodcast.sh`
4. The first prompt will ask you for the name of the podcast.  This is the part of the URL Mentioned in step 1.  
    `Enter the part of the URL for the podcast after the v= :`  
5. The second and final prompt will as you for the episode number enter it and press enter  
    `Enter the podcast number:`
6. Press enter and let it run.