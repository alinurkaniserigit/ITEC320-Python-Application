from tkinter import END, Button, Entry, Tk
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import requests
import json
import datetime
import time
from googletrans import Translator
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Initialize speech recognition engine
r = sr.Recognizer()

# Initialize translator
translator = Translator()

def speak(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def get_audio():
    """Function to get audio input from user"""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        speak("Sorry, I could not understand you. Please try again.")
    except sr.RequestError as e:
        speak(f"Sorry, there was an error with the speech recognition service: {e}")
def handle_commands(user_input):
    """Function to handle user commands"""
    if not user_input:
        return
    if "hello" in user_input.lower():
        speak("Hello! How can I assist you?")
    # rest of the code

def handle_commands():
    """Function to handle user commands"""
    speak("I'm listening...")
    user_input = get_audio()
    if not user_input:
        return
    if "hello" in user_input.lower():
        speak("Hello! How can I assist you?")
    elif "what is the capital of" in user_input.lower():
        country = user_input.split()[-1]
        wikipedia.set_lang("en")
        capital = wikipedia.page(f"{country} capital").content.split("\n")[0]
        speak(f"The capital of {country} is {capital}")
    elif "weather" in user_input.lower():
        try:
            city = user_input.split()[-1]
            weather_api_key = "your_api_key"
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
            response = requests.get(weather_url)
            weather_data = json.loads(response.text)
            temperature = weather_data['main']['temp']
            weather_description = weather_data['weather'][0]['description']
            speak(f"The temperature in {city} is {temperature} degrees Celsius with {weather_description}")
        except:
            speak("Sorry, I could not get the weather information for that location.")
    elif "play music" in user_input.lower():
        # code for playing music
        speak("What would you like me to play?")
        music_name = get_audio()
        music_url = f"https://www.youtube.com/results?search_query={music_name}"
        webbrowser.get().open(music_url)
    elif "set alarm" in user_input.lower():
        # code for setting alarm
        speak("At what time do you want me to set the alarm?")
        alarm_time = get_audio()
        try:
            alarm_time = datetime.datetime.strptime(alarm_time, '%H:%M')
            while True:
                current_time = datetime.datetime.now().strftime("%H:%M")
                if current_time == alarm_time.strftime("%H:%M"):
                    speak("Wake up!")
                    break
                time.sleep(60)
        except ValueError:
            speak("Sorry, I couldn't understand the time.")
    elif "search" in user_input.lower():
        search_engine = ""
        if "google" in user_input.lower():
            search_engine = "https://www.google.com/search?q="
        elif "bing" in user_input.lower():
            search_engine = "https://www.bing.com/search?q="
        else:
            speak("Sorry, I could not find the specified search engine.")
        if search_engine:
            query = user_input.split("search")[-1].strip()
            query_url = search_engine + query.replace(" ", "+")
            webbrowser.get().open(query_url)
    elif "translate" in user_input.lower():
        try:
            source_language = user_input.split()[-2]
            target_language = user_input.split()[-1]
            text_to_translate = user_input.split()[1:-2]
            text_to_translate = " ".join(text_to_translate)
            translation = translator.translate(text_to_translate, src=source_language, dest=target_language)
            speak(f"The translated text is {translation.text}")
        except:
            speak("Sorry, I could not translate the text. Please try again.")
    else:
        wikipedia.set_lang("en")
        try:
            page = wikipedia.page(user_input)
            summary = wikipedia.summary(user_input, sentences=2)
            speak(summary)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Can you please be more specific?")
        except wikipedia.exceptions.PageError as e:
            speak("Sorry, I could not find any information on that topic.")


# Create the main window of the application
window = Tk()
window.title("AI Assistant")
window.geometry("500x500")

# Start the main event loop
window.mainloop()