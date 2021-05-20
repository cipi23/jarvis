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
        elif 'how are you' in recorded_audio:
            speak("I am fine...")  
        
        # get today's date
        elif 'date' in recorded_audio:
            speak("The date is" + get_date()) 

        # get current time 
        elif 'time' in recorded_audio:
            speak("The time is " + get_time())
        
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
            ipt_input(recorded_audio)

        #close a port
        elif 'block' in recorded_audio:
            ipt_block(recorded_audio)

        #set ip for nmap
        elif 'set' in recorded_audio:
            speak("What ip do you want to scan? ")
            host = recordAudio()
            print("the ip is: ",host)

        #nmap module
        elif 'scan' in recorded_audio:
            nmap_scan('tcp',host)

        elif 'scam' in recorded_audio:
            nmap_scan('tcp',host)
        
        elif 'come' in recorded_audio:
            nmap_scan('tcp',host)

        #monitor logs
        elif 'monitor log' in recorded_audio:
            log_monitor()
            
        elif 'show last log' in recorded_audio:
            last_log()
            
        #iptables route
        elif 'route' in recorded_audio:
            ipt_route(recorded_audio)

    except Exception:
        print("Bob dont understand you, plz try again...")
        
