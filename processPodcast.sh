#!/bin/bash
# This is the wrapper for the Fabric process to get the podcast
# process it and add it to the repository.

# Variables
DIR=$(cd $(dirname $0);pwd)
LOGDIR=${DIR}/logs
DATE=$(date +%Y%m%d_%H%M)
OUTPUTLOG=${LOGDIR}/${DATE}.output.log

#Make logs directory
if [ ! -d ${LOGDIR} ]
then
    mkdir -p ${LOGDIR}
fi

read -p "Enter the part of the URL for the podcast after the v= : " -a URLName
read -p "Enter the podcast number: " -a podcastNumber

episodeName="linuxinstall.net."${podcastNumber}

echo "Command being run:"|tee ${OUTPUTLOG}
echo fab convert_podcast:podcastName="${episodeName}",videoName="${URLName}",outputdir="${DIR}/${episodeName}"|tee ${OUTPUTLOG}
fab convert_podcast:podcastName="${episodeName}",videoName="${URLName}",outputdir="${DIR}/${episodeName}"|tee ${OUTPUTLOG}