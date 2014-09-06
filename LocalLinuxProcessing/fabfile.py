#!/usr/bin/env python
from fabric.api import *
import os

@hosts('localhost')
def download_from_YouTube(theDownload=None,outputFile=None):
    try:
        if not theDownload is None and not outputFile is None:
            theURL="http://www.youtube.com/watch?v=%s" % theDownload
            #print theURL
            theCommand=("youtube-dl -f 18 %s -o '%s'" % (theURL,outputFile))
            output=run(theCommand)
            if "has already been downloaded" in output:
                print "Youtube this file has been downloaded already?"
                exit
        else:
            print "Download name not provided"
            exit
    except:
        exit

@hosts('localhost')
def convert_to_FLAC(inputFile=None,outputFile=None):
    try:
        if not inputFile is None and not outputFile is None:
            theCommand=('avconv -i %s -acodec flac %s' % (inputFile,outputFile))
            run(theCommand)
        else:
            print "File names were not provided"
            exit
    except:
        exit

@hosts('localhost')
def convert_to_MP3(inputFile=None,outputFile=None):
    try:
        if not inputFile is None and not outputFile is None:
            theCommand=('avconv -i %s -ab 64k -ac 2 -ar 48000 %s' % (inputFile,outputFile))
            run(theCommand)
        else:
            print "File names were not provided"
            exit
    except:
        exit

@hosts('localhost')
def normalize_audio(inputFile=None,normalizeName=None):
    try:
        if not inputFile is None:
            theCommand=("sox -G --norm --magic -S -c 1 %s -t flac %s" % (inputFile,normalizeName))
            run(theCommand)
        else:
            print "File Name not provided"
            exit
    except:
        exit

@hosts('localhost')
def convert_podcast(videoName=None,podcastName=None,outputdir=None):
    try:
        if not outputdir is None:
            if not os.path.exists(outputdir):
                os.makedirs(outputdir)
                if not os.path.exists(outputdir):
                    print "Couldn't create output directory."
                    exit
            if not videoName is None:
                inputName=("%s/%s.mp4" % (outputdir,videoName))
                outputName=("%s/%s.flac" % (outputdir,videoName))
                normalizeName=("%s/%s.normal.flac" % (outputdir,videoName))
                podcastFile=("%s/%s.mp3" % (outputdir,podcastName))
                download_from_YouTube(videoName,inputName)
                convert_to_FLAC(inputName,outputName)
                normalize_audio(outputName,normalizeName)
                convert_to_MP3(outputName,podcastFile)
            else:
                print "Missing videoName or podcastName"
                exit
    except:
        raise
        exit   

