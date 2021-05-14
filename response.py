from datetime import datetime
import pyttsx3
from linux_utilities import *


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)


def speak(audio):
  engine.say(audio)
  engine.runAndWait()

