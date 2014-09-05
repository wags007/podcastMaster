__author__ = 'bwagner'
import sys, argparse
import json
#from fabric.api import *

try:
    import requests
    from requests.auth import HTTPBasicAuth

    # if int(requests.__version__.split('.')[1]) < 12:
    #     print "You may have to upgrade your python requests version!"

except:
    print "Please install python requests!"
    print "Instructions can be found here:"
    print "http://docs.python-requests.org/en/latest/user/install/"

# Auphonic API url
API_URL = "https://auphonic.com/api/simple/productions.json"
SERVICES_URL = "https://auphonic.com/api/services.json"

def Get_Services(username,password):
    try:
        result = requests.get(SERVICES_URL,auth=HTTPBasicAuth(str(username),str(password)))
        if result.status_code == 200:
            print "We got %s" % str(result.status_code)
            #print result.json()
            Services = result.json()
            return Services[u'data']
        else:
            print "We got a non-200 response: %s" % result.status_code
            raise IOError("Failed to connect to the Auphonic Service")
    except:
        raise



def main(argv):
        argumentParser = argparse.ArgumentParser(description='Script to pull Hangouts from Youtube and push them to Auphonic')
        argumentParser.add_argument('--episode-regex',dest='epregex',default='*',
                                    help='If you want to find an episode by regex expression')
        argumentParser.add_argument('--outputname',dest='outputname',default='None',
                                    help='The name of the file to be uploaded')
        argumentParser.add_argument('--channel-url',dest='channelUrl',default='None',
                                    help='The location of your channel on youtube')
        args = argumentParser.parse_args()
        print args.epregex
        print args.outputname
        print args.channelUrl

if __name__ == "__main__":
        main(sys.argv[1:])
        try:
            ServiceList = Get_Services("wags007@gmail.com","69dpRSTsNKlv")
        except Exception as e:
            raise type(e)(e.message)

        ServiceCount = 0
        print "Available Services:"
        #print "     Type : UUID"
        while ServiceCount < len(ServiceList):
            ServiceDict = ServiceList[ServiceCount]
            print ("     %s : %s " % (ServiceDict["type"], ServiceDict['uuid']))
            ServiceCount = ServiceCount + 1
