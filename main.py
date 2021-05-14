from recordaudio import recordAudio
from nmap_mod import nmap_scan
from linux_utilities import *
from response import *
from programs import *
from firewall import *
from log import *


while True:
    try:
        recorded_audio = recordAudio()

        if "name" in recorded_audio:
            speak("My name is Bob")
  
        # how are you?
        if "how are you" in recorded_audio:
            speak("I am fine...")  
            # date
        if "date" in recorded_audio:
            # get today's date
            speak("The date is" + get_date()) 
            # time
        if "time" in recorded_audio:
            # get current time 
            speak("The time is " + get_time())

        #set ip for nmap
        if ' set ' in recorded_audio:
            host = input("What ip do you want to scan? ")

        #nmap module
        elif 'scan' in recorded_audio:
            nmap_scan(recorded_audio,host)
        
        #linux_utilitie module (grep)
        elif 'find' in recorded_audio:
            grep(recorded_audio)

        #linux_utilities module (cat)
        elif 'cat ' in recorded_audio:
            cat(recorded_audio)
        
        #open a program
        elif 'open' in recorded_audio:
            open(recorded_audio)
        
        #open new terminal and change directory
        elif 'go to' in recorded_audio:
            cd(recorded_audio)

        #find something in google
        elif 'google' in recorded_audio:
            web(recorded_audio)

        #open a port from incoming traffic
        elif 'accept' in recorded_audio:
            ipt_input()

        #close a port
        elif 'block' in recorded_audio:
            ipt_block()


        elif 'monitor log' in recorded_audio:
            log_monitor()
            
        elif 'show last log' in recorded_audio:
            last_log()


    except Exception:
        print("Bob dont understand you, plz try again...")
        
