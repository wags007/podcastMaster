# This file creates a docker image for PodcastMaster
#FROM ubuntu:14.04
FROM phusion/baseimage:latest
MAINTAINER Brian Wagner <wags007@gmail.com>
# Set correct environment variables.
ENV HOME /root
ENV TERM linux
ENV DEBIAN_FRONTEND noninteractive
# Regenerate SSH host keys. baseimage-docker does not contain any, so you
# have to do that yourself. You may also comment out this instruction; the
# init system will auto-generate one during boot.
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
RUN sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile
RUN apt-get update && \
    apt-get install -y libav-tools sox python2.7 wget git curl openssh-server python-dev
RUN wget https://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg && \
    sh setuptools-0.6c11-py2.7.egg &&\
    wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py &&\
    python2.7 get-pip.py && \
    pip install fabric==1.8.1 && \
    pip install --upgrade youtube_dl
#Setup SSH
# Turn off ssh key checking since the script only ever connects to itself
RUN echo StrictHostKeyChecking no >>/etc/ssh/ssh_config
# Create your SSH Keys for connecting back to yourself
RUN  mkdir -p .ssh && \
     ssh-keygen -b 1024 -f /root/.ssh/id_rsa -N "" && \
     cp -a /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys
# Grab the scripts from GitHub
RUN git clone https://github.com/wags007/podcastMaster.git

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME ["~/output:/podcastMaster/LocalLinuxProcessing/output"]
CMD ["/podcastMaster/LocalLinuxProcessing/processPodcast.sh"]