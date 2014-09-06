#!/bin/bash
# This is the wrapper for the Fabric process to get the podcast
# process it and add it to the repository.

# Variables
DIR=$(cd $(dirname $0);pwd)
LOGDIR=${DIR}/output/logs
DATE=$(date +%Y%m%d_%H%M)
OUTPUTLOG=${LOGDIR}/${DATE}.output.log

#Make logs directory
if [ ! -d ${LOGDIR} ]
then
    mkdir -p ${LOGDIR}
fi

read -p "Enter the part of the URL for the podcast after the v= : " -a URLName
read -p "Enter the podcast number: " -a podcastNumber
read -p "Enter the podcast name: " -a podcastName

episodeName=${podcastName}"."${podcastNumber}

echo "Command being run:"|tee ${OUTPUTLOG}
echo fab convert_podcast:podcastName="${episodeName}",videoName="${URLName}",outputdir="${DIR}/output/${episodeName}"|tee ${OUTPUTLOG}
fab convert_podcast:podcastName="${episodeName}",videoName="${URLName}",outputdir="${DIR}/output/${episodeName}"|tee ${OUTPUTLOG}
