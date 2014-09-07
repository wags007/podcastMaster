#!/bin/bash
# The following lines are used for local testing
#echo "REPOSITORY              TAG                 IMAGE ID            CREATED             VIRTUAL SIZE"
#docker images|grep -i podcastmaster
#read -p "Docker Image ID: " -a imageID

baseDir=$(cd $(dirname ~/output);pwd)
outputDir="${baseDir}/output"
if [ ! -d ${outputDir} ]
then
    mkdir -p ${outputDir}
fi

# The following line is used for local testing
#docker run --rm -t -i -v ${outputDir}:/podcastMaster/docker_image/output imageID
docker run --rm -t -i -v ${outputDir}:/podcastMaster/docker_image/output wags007/podcastmaster
