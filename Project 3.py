'''How can I build a Python-based voice assistant that activates on a wake word
like 'Jarvis', responds via speech, and executes simple voice commands 
like opening websites or playing songs from a custom music library

This code implements a full voice assistant that:
Uses speech recognition to listen and transcribe audio
Has a wake word system
Responds with text-to-speech
Can open websites based on voice commands
Can play songs from a predefined musiclibrary'''
#***********************************************************************************************
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
#pip install pocketsphinx
recognizer=sr.Recognizer()
#ttsx=pyttsx3.init()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open gmail" in c.lower():
        webbrowser.opem("http://gmail.com")
    elif "open facebook" in c.lower():
        webbrowser,open("http//facebook.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
if __name__=="__main__":
    speak("Initializing Jarvis......")
    while True:
        # copy from speechrecognition python 3.1.2 Example: https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
        #listen for the wake word "jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("recognizing...")# ecognize is use to  how much time is taking to listen
        # recognize speech using Sphinx
        try:
            #    pip install google-cloud-speech
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=4,phrase_time_limit=2) #set to taking time limit 2sec
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source) #set to taking time limit 2sec
                    
                    command=r.recognize_google(audio)
                    processCommand(command)
            
        except Exception as e:
            print("Error; {0}".format(e)) #last
