#!/usr/bin/python

import sys
import socket
import getopt
import threading
import subprocess

#DEFINE SOME GLOBAL VARIABLES
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


def usage():
    print(" NetKnife ----")
    print
    print("Usage:python3 NetKnife.py -t target_host -p port")
    print("-l --listen                  -Listen on [host]:[port] for incoming connection")
    print("-e --execute=file_to_run     -Execute the given file upon receiving a connection")
    print("-c --command                 -Initialize a command shell")
    print("-u --uploa=destination       -Upon receiving a connection upload a file and write to [destination]")
    print
    print
    sys.exit(0)


def main():
    global listen 
    global port 
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    #READ THE COMMANDLINE OPTIONS
    try:
        opts,args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute=","target=","port=","command","upload="])
    except getopt.GetoptError as err:
        print("Erreur")
        usage()

    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e","--execute"):
            execute = a
        elif o in ("-c","--command"):
            command = True
        elif o in ("-u","--upload"):
            upload_destination = a
        elif o in ("-t","--target"):
            target = a
        elif o in ("-p","--port"):
            port = int(a)
        else:
            print("UNHANDLED OPTIONS")
        

    if not listen and len(target) and port > 0:
        buffer = sys.stdin.read()

        #SEND DATA OFF
        client_sender(buffer)
    #WE ARE GOING TO LISTEN ,UPLOAD THINGS ,EXECUTE COMMANDS
    #DROP A SHELL BACK DEPENDING ON OUR COMMAND LINE OPTIONS ABOVE
    if listen :
        server_loop()

main()
