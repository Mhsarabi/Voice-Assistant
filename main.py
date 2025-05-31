import cv2
import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # for rate
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)  # for male


def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def take_command():
    take = sr.Recognizer()

    with sr.Microphone(device_index=0) as source:
        print("listening...")
        audio = take.listen(source)

        try:
            command = take.recognize_google(audio, language="en-US")
            print(f"you said: {command}\n")
            speak(f"you said: {command}")

        except:
            print("sorry,I didn't underestand,pleas say again...\n")
            speak("sorry,I didn't underestand,pleas say again.")
            return "None"
    return command

NAME = "mohsen"


def welcome():
    hour = datetime.datetime.now().hour
    if 0 <= hour <= 12:
        print("hello , good morning.\n")
        speak("hello , good morning.")

    elif 12 < hour <= 18:
        print("hello , good afternoon.\n")
        speak("hello , good afternoon.")

    else:
        print("hello , good night.\n")
        speak("hello , good night.")

    print("what is your name?\n")
    speak("what is your name?")
    global NAME
    while True:
        NAME = take_command().lower()
        if NAME != "none":
            break

    print(f"welcome {NAME}.lets start!\n")
    speak(f"welcome {NAME}.lets start!\n")

welcome()