# This file creates a docker image for PodcastMaster
FROM python:3.9-slim
# Set correct environment variables.
ENV HOME /root
ENV TERM linux
ENV DEBIAN_FRONTEND noninteractive

COPY requirements.txt /tmp/pip-tmp/
RUN sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile
RUN apt update && apt upgrade -y && \
    apt install -y ffmpeg sox wget git curl python3-pip

RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

#Setup SSH
# Turn off ssh key checking since the script only ever connects to itself
#RUN echo StrictHostKeyChecking no >>/etc/ssh/ssh_config
# Create your SSH Keys for connecting back to yourself
#RUN  mkdir -p .ssh && \
#     ssh-keygen -b 1024 -f /root/.ssh/id_rsa -N "" && \
#     cp -a /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys
# Grab the scripts from GitHub
COPY https://github.com/wags007/podcastMaster.git ~/

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME ["~/output:/podcastMaster/docker_image/output"]
CMD ["/podcastMaster/docker_image/processPodcast.sh"]