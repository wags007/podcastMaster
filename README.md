# Podcast Master
---
## A tool for turning Google Hangouts into Audio Podcasts
---
This set of scripts is something designed to make the tedious process of migrating my podcasts from G+ Hangouts On-Air to usable audio podcasts.  Their are two ways I have been doing this:

1. Using some linux tools like FFMPeg and SOX to do all the migrations on my local system.  The files for this are under the LocalLinuxProcessing Directory.
2. Is to pull the audio from the Youtube Video a push it up to Auphonics.  They then process it and upload it to


Please feel free to clone, enhance, or write additional ways to process audio files and give me pull requests.  If you use them and like them please let me know that also at feedback at devopsmastery dot com

---
## New Feature
---
Not that the script is that hard to setup but I wanted something to do with Docker.io.  So I set it up and then migrated this applciation from the Linux Local Processing directory.  I have now released a [Docker image located here](https://registry.hub.docker.com/u/wags007/podcastmaster/).  Once you have Docker setup you really only need to run the command `docker-processPodcast.sh`  That script will pull down the proper image and run the script.  All you have to do is follow the prompts and check out the resutling podcast in your home directory under a subdirectory called output.  There will then be the working directory which is based on the name of the podcast and podcast number.  So now you can try it out with nearly no work on your part. So enjoy and tell me how I could make it better.