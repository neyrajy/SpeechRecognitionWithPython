import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime
import time
from playsound import playsound
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def my_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command


def run_alexa():
    command = my_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.now().strftime('%I:%M %p')
        print(current_time)
        talk('The current time is ' + current_time)
    elif 'alarm' in command:
        alarm = "12:44"
        while True:
            local_time = datetime.now().strftime('%H:%M')
            if local_time == alarm:
                print(alarm)
                talk('Hey you its time to wake up ' + alarm)
                playsound("alarm.mp3")
                break
            else:
                print('Not yet! The time is ' + datetime.now().strftime('%H:%M'))
                time.sleep(10)
    elif 'day' in command:
        day = datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
            talk("Today is " + day_of_the_week)
    
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Sorry, I didn't get that. Please try again")


while True:
    run_alexa()