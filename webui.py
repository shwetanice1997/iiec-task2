import speech_recognition as sr
import webbrowser
import pyttsx3
print()
print("Here is the Program which run Linux Command as well as Launch the Docker Container ")
print()
pyttsx3.speak("Hello I am Maira")
pyttsx3.speak("I am here to help you to run Linux Command as well as launch docker container")
pyttsx3.speak("Tell me your requirement") 
r=sr.Recognizer()
with sr.Microphone() as source:
  print("I am Listening to You....")
  audio=r.listen(source)
  print("Done...")
text=r.recognize_google(audio)
print(text)

if (("run" in text) or ("launch" in text)) and (("docker" in text) or ("container" in text)):
  webbrowser.open("http://192.168.43.98/drun.html")
  pyttsx3.speak("Opening a Page  to launch Docker")
elif (("run" in text) or ("launch" in text) and ("Linux" in text) or ("commands" in text)):
  webbrowser.open("http://192.168.43.98/webapp.html")
  pyttsx3.speak("Opening a Page Run Linux Commands")
else:
  print("Sorry")