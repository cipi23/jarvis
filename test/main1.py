import speech_recognition as sr 

r = sr.Recognizer()
with sr.Microphone() as source:
	while True:
		try:
			print("listening...")
			audio = r.listen(source)
			q = r.recognize_google(audio, language = "en")
			print("you said: " + q.lower())
			if "youtube" in q.lower():
				print("open youtube")
		except:
			pass
