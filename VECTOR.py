import ctypes
import datetime
import os
import sys
import webbrowser
from subprocess import *
from tkinter import *
import pyttsx3
import speech_recognition as sr
import wikipedia
from openfile import searchfiles

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def main_screen(welcome):
    print(welcome)

    root = Tk()
    root.title('Vector Assistant')
    root.configure(bg='#BCD5E5')
    root.geometry('350x500')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else :
        speak("Good Evening!")

    speak("I am Vector.")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #will recognize voice and convert to text.
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    WishMe()
    
WAKE = "hi vector" #will only implement commands after hearing this.
while True:
    
    query = takeCommand().lower()

    if query.count(WAKE) > 0: 
        #if count of wake is more than 0 than it will speak.
        speak("Hello Vaibhav Sir, Nice to be back with you. Please tell how may i help you.")

        while True:

            query = takeCommand().lower() #This query will take below logics.
            
            #Logic for execution tasks based on query
            if 'wikipedia' in query:
                speak("Searching in Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("Accordin to Wikipedia")
                print(results)
                speak(results)
        
            elif 'open google' in query:
                webbrowser.open("google.com")
                speak("opening google")
        
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")  
                speak("opening youtube") 
        
            elif 'play music' in query:
                music_dir = 'C:\\Users\91937\Music'
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[0]))
                speak("Playing song")
        
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir, the time is {strTime}")
                print(strTime)
        
            elif 'open vs code' in query:
                codePath = "C:\\Users\\91937\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                speak("opening vs code")
        
            elif 'open C Drive' in query:
                codePath = "C:\\"
                os.startfile(codePath)
                speak("opening C drive")
        
            elif 'file' in query:
                l = query.split()
                file_name = l[-1]
                print(file_name)
                s = "searching for the file" +file_name
                speak(s)
                try:
                    result="path is"+ searchfiles(file_name)
                    speak(f"{file_name} file has been found")
                except Exception as e:
                    speak("Sorry! file not found")
                print(file_name)
        
            elif 'lock my laptop' in query:
                ctypes.windll.user32.LockWorkStation()
                speak("locking your laptop sir")

            elif 'exit' in query: #this will be implemet after waking.
                speak("Bye sir! Have a great day.")
                sys.exit(0)
                
    
    elif 'stop' in query: #This will get implement before waking.
        sys.exit(0)
