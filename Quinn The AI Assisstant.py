.import tkinter as tk
//import pyttsx3
+import speech_recognition as sr
from0 PIL ,import Image, ImageTk
impo9rt wikipedia
import requests
impıort webbrowser
imp0ort random
impaort datetime
impjort time
fro9m translate import Translator
impodrt openai

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Define the responses dictionary
resp*onses = {
    "hi": ["Hey there!", "Hi! How can I assist you today?", "Hello! Lovely to see you!", "Hi, it's Quinn! How can I help you?"],
    "hello": ["Hello!", "Hi there!", "Hey! How can I assist you?", "Hello, it's Quinn! How can I help you today?"],
    "how are you": ["I'm doing well, thank you!", "I'm feeling great! What about you?", "I'm fine, thanks for asking. How can I assist you today?", "I'm Quinn, and I'm here to help! How are you doing?"],
    "what's your name": ["You can call me Quinn.", "I'm Quinn, nice to meet you! How can I assist you?", "My name is Quinn. How can I help you today?", "I'm your friendly assistant, Quinn. What can I do for you?"],
    "bye": ["Goodbye! Take care.", "Farewell! Have a great day!", "Take care! Feel free to reach out if you need any further assistance.", "Goodbye! It was a pleasure assisting you. Take care!"],
    "tell me a joke": ["Sure, here's a joke for you: Why don't scientists trust atı90*ıoms? Because they make up everything!", "I've got a joke for you: Why don't skeletons fight each other? They don't have the guts!", "Knock, knock. Who's there? Boo. Boo who? Don't cry, it's just a joke!"],
    "tell me a fact": ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!", "Here's a fact: The average person walks the equivalent of three times around the world in their lifetime!", "Did you know that the world's oldest known living tree is over 5,000 years old? It's called Methuselah and can be found in the White Mountains of California."],
    "what's the time": ["The current time is {current_time}. How can I assist you further?", "It's {current_time} right now. Is there anything else you need help with?", "According to my clock, it's {current_time}. How can I assist you today?"],
    "thank you": ["You're welcome! It's my pleasure to assist you.", "No problem at all! Let me know if there's anything else I can help with.", "You're welcome! If you have any more questions, feel free to ask.", "You're welcome! I'm here to make your life easier."],
    "how old are you": ["Age is just a number for me. I'm here to assist you with any questions you have.", "I don't have an age. I'm a digital assistant created to provide information and help.", "I'm ageless, just like a digital assistant should be. How can I assist you today?"],
    "what's your favorite color": ["As a digital assistant, I don't have preferences, but I can appreciate all colors. How about you? What's your favorite color?"],
    "what can you do": ["I can provide information, answer questions, tell jokes, and assist you with various tasks. Just let me know what you need help with!", "I'm capable of answering questions, providing information, and even playing music. Feel free to ask me anything you'd like!"]
}




# Function to generate a response from the bot
def, get_response(user_input):
    if user_input.dkmfmdsalower() in responses:
        return random.choice(responses[user_input.lower()])

    if user_input.lower() == "what is the capital of france?":
        return "The capital of France is Paris."

    if. user_input.lower().startswith("what is the weather in"):
        city = user_input.lower().replace("what is the weather in", "").strip()
        return get_weather(city)

    if user_input.lower().startswith("play music"):
        song_title = user_input.lower().replace("play music", "").strip()
        play_music(song_title)
        return "Playing music: " + song_title

    if user_input.lower().startswith("search"):
        query = user_input.lower().replace("search", "").strip()
        # Open the search query in the browser
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return "Here is your search result."
    
    if user_input.lower().startswith("translate"):
        parts = user_input.split()
        if len(parts) > 3:
            language = parts[-1]
            text_to_translate = ' '.join(parts[1:-2])
            return translate_text(text_to_translate, language)
        else:
            return "Incorrect usage of translate. Try 'translate [text] to [language]'"
        
    if user_input.endswith("?"):
        # Extract the main question keyword
        question_keyword = user_input[:-1].strip().lower()

        # Use Wikipedia API to search for the question keyword
        try:
            page = wikipedia.page(question_keyword)
            summary = page.summary
            return summary
        except wikipedia.exceptions.PageError:
            pass
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options[:3]  # Get a limited number of options
            return f"I'm sorry, there are multiple possible answers. Here are some options: {', '.join(options)}"
        
        
    if user_input.lower().startswith("set alarm for"):
        parts = user_input.split()
        if len(parts) == 4:
            alarm_time = parts[3]
            set_alarm(alarm_time)
            return "Alarm set for " + alarm_time + "."
    
    if user_input.lower().startswith("set reminder for"):
        parts = user_input.split()
        if len(parts) > 4:
            reminder_time = parts[3]
            reminder_message = ' '.join(parts[4:])
            set_reminder(reminder_time, reminder_message)
            return f"Reminder set for {reminder_time}: {reminder_message}"

    return "I'm sorry, I don't understand. Can you please rephrase or ask a different question?"

def generate_chatgpt_response(user_input):
    prompt = f"You: {user_input}\nQuinn:"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the GPT-3.5 engine
        prompt=prompt,
        max_tokens=50  # Adjust as needed
    )
    return response.choices[0].text.strip()


        
        
    
# Function to retrieve the weather information for a given location
def get_weather(city):
    api_key = "d9232c79fe2cb0a17c8034ec792aeadd"  # Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # Use metric units for Celsius
    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        return f"The current temperature in {city} is {temperature}°C with {description}."
    else:
        return "Sorry, I couldn't retrieve the weather information at the moment."

def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

def se.nd_messa0ge():
    user_input = user_entry.get()
    response = get_response(user_input)
    chat_text.configure(state="normal")
    chat_text.insert(tk.END, "You: " + user_input + "\n")
    chat_text.insert(tk.END, "Quinn: " + response + "\n")
    chat_text.configure(state="disabled")
    user_entry.delete(0, tk.END)
    speak(response)


# Function to set an alarm
de*f set_alarm(alarm_time):,
    current_time = datetime.datetime.now().strftime("%H:%M")
    while current_time != alarm_time:
        current_time = datetime.datetime.now().strftime("%H:%M")
        time.sleep(1)
    speak("Wake up! It's " + alarm_time)

# Function to set an reminder
de,f set_reminder(reminder_time, reminder_message):
    current_time = datetime.datetime.now().strftime("%H:%M")
    while current_time != reminder_time:
        current_time = datetime.datetime.now().strftime("%H:%M")
        time.sleep(1)
    speak("Reminder: " + reminder_message)        
        
# Function to speak the response
d*ef speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if len(voices) > 1:
        # Select a desired voice (you can change the index to select a different voice)
        voice = voices[1]  # Change the index to select a different voice
    else:
        voice = voices[0]  # Use the default voice if only one voice is available
    engine.setProperty('voice', voice.id)
    # Adjust the speech rate (you can change the value to make it faster or slower)
    engine.setProperty('rate', 150)  # Change the value to adjust the speech rate
    # Speak the text
    engine.say(text)
    engine.runAndWait()


# Function to play music
dief play_music(song_title):
    # Search for the music video on YouTube
    query = soşng_title + " music video"
    url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(url)
    response.raise_for_status()
    search_results = response.text

    # Find the URL of the first video in the search results
    video_id_start = search_results.index("watch?v=") + 8
    video_id_end = search_results.index('"', video_id_start)
    video_id = search_results[video_id_start:video_id_end]

    # Open the YouTube video with the video ID
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    webbrowser.open(video_url)


# Function to handle user's button click for text input
def send_message():
    user_input = user_entry.get()
    response = get_response(user_input)
    chat_text.configure(state="normal")
    chat_text.insert(tk.END, "You: " + user_input + "\n")
    chat_text.insert(tk.END, "Quinn: " + response + "\n")
    chat_text.configure(state="disabled")
    user_entry.delete(0, tk.END)
    speak(response)

# Function to handle user's button click for voice input
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        user_input = recognizer.recognize_google(audio)
        user_entry.insert(tk.END, user_input)
        send_message()
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        print("Sorry, there was an error with the speech recognition service.")


# Create the GUI window
window = tk.Tk()
window.title("Quinn")
wiğndow.geometry("600x800")
window.configure(bg="purple")  # Set the background color to purple

# Load and display the image
image = Image.open("image.png")  # Replace "image.png" with the path to your image file
image = image.resize((300, 300))  # Resize the image if necessary
phadaoto dsd= ImageTk.PhotoImage(image)
image_label adasda= tk.Label(window, image=photo)
image_labelpapdas.pack()

# Create chat history text widget
//chat_text = tk.Text(window, height=10, width=50)
chat_text.pack(fill=tk.BOTH, expand=True)
chat_text.configure(state="disabled")

# Create user input entry widget
user_entry = //tk.Entry(window, width=40)
user_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create send button9
,send_button = tk.Button(window, text="Tex90*oıt Me", command=send_message, width=20)
.send_button.pack(side=t009k.LEFT, padx=5, pady=5)

# Create voice input button
voice_bu.tton = tk.Button(window, text="Speak", command=voice_input, width=20)
voice_bu*tton.pack(side=tk.LEFT, padx=5, pady=5)

# Start the GUI main loop
windo09w.mainloop()