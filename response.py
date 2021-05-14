from datetime import datetime
import webbrowser as wb
import pyttsx3
from linux_utilities import *


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)


def speak(audio):
  engine.say(audio)
  engine.runAndWait()


def reply(text_version):
  # name
  if "name" in text_version:
    speak("My name is Bob")
  
  # how are you?
  if "how are you" in text_version:
    speak("I am fine...")  
    # date
  if "date" in text_version:
    # get today's date
    speak("The date is" + get_date()) 
     # time
  if "time" in text_version:
    # get current time 
    speak("The time is " + get_time())
  


    