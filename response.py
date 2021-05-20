import pyttsx3

#initialize pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

#speak function
def speak(audio):
  engine.say(audio)
  engine.runAndWait()

