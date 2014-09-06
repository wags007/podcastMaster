# This file creates a docker image for PodcastMaster
FROM ubuntu:14.04
MAINTAINER Brian Wagner <wags007@gmail.com>
RUN apt-get update && apt-get install -y etckeeper
RUN apt-get update && apt-get install -y libav-tools sox python2.7 wget git curl
RUN wget https://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg && sh setuptools-0.6c11-py2.7.egg && wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py && python get-pip.py &&  pip install fabric
RUN git clone https://github.com/wags007/podcastMaster.git
