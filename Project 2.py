'''How can I create a simple voice assistant in Python that greets the user using
text-to-speech when the program starts'''
#******************************************************************************************************   
import speech_recognition as sr
import webbrowser
import pyttsx3
recognizer=sr.Recognizer()
#ttsx=pyttsx3.init()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
if __name__=="__main__":
    speak("hey sir how may i help you")

