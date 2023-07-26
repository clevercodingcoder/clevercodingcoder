import sys
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import pytz
import requests
import webbrowser
import random
from googletrans import Translator
import time

# Text-to-speech setup
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Weather API setup
def get_weather_info():
    api_key = "api key"  # Replace this with your OpenWeatherMap API key
    city = "City name"  # Replace this with your desired city name
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") == "404":
        speak("City not found. Please check the city name.")
    else:
        try:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            temp_celsius = temperature - 273.15
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            speak(f"The weather in {city} is currently {weather_description}.")
            speak(f"The temperature is {temp_celsius:.2f} degrees Celsius.")
            speak(f"The humidity is {humidity}%.")
            speak(f"The wind speed is {wind_speed} meters per second.")
        except KeyError:
            speak("Sorry, I couldn't retrieve the weather information at the moment. Please try again later.")

# Get time
def get_time():
    tz = pytz.timezone('Europe/Berlin')  # Replace 'Europe/Berlin' with your desired timezone
    current_time = datetime.datetime.now(tz).strftime("%H:%M")
    speak(f"The current time is {current_time}.")

# Get current date
def get_date():
    tz = pytz.timezone('Europe/Berlin')  # Replace 'Europe/Berlin' with your desired timezone
    current_date = datetime.datetime.now(tz).strftime("%Y-%m-%d")
    speak(f"Today's date is {current_date}.")

# Get date for tomorrow
def get_tomorrow_date():
    tz = pytz.timezone('Europe/Berlin')  # Replace 'Europe/Berlin' with your desired timezone
    tomorrow_date = datetime.datetime.now(tz) + datetime.timedelta(days=1)
    formatted_date = tomorrow_date.strftime("%Y-%m-%d")
    speak(f"Tomorrow's date is {formatted_date}.")

# Extract days from "date in X days" query
def extract_days_from_query(query):
    days = None
    words = query.split()
    for i in range(len(words)):
        if words[i] == "in" and i < len(words) - 1:
            try:
                days = int(words[i + 1])
            except ValueError:
                pass
            break
    return days

# Get date for X days in the future
def get_date_in_days(query):
    days = extract_days_from_query(query)
    if days is not None:
        tz = pytz.timezone('Europe/Berlin')  # Replace 'Europe/Berlin' with your desired timezone
        future_date = datetime.datetime.now(tz) + datetime.timedelta(days=days)
        formatted_date = future_date.strftime("%Y-%m-%d")
        speak(f"The date {days} days from now will be {formatted_date}.")
    else:
        speak("Sorry, I couldn't understand the number of days. Please try again.")

# Take notes
def take_notes():
    notes = []
    
    speak("What should the note be called?")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    
    try:
        note_title = recognizer.recognize_google(audio, language='en').lower()
        print("User (Note Title):", note_title)
        if "stop" in note_title or "done" in note_title:
            return
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you. Could you please repeat?")
        speak("Sorry, I couldn't understand you. Could you please repeat?")
        return
    
    speak("What should I write in the note?")
    while True:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)
        
        try:
            note_text = recognizer.recognize_google(audio, language='en').lower()
            print("User (Note Text):", note_text)
            if "stop" in note_text or "done" in note_text:
                break
            notes.append(note_text)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand you. Could you please repeat?")
            speak("Sorry, I couldn't understand you. Could you please repeat?")
    
    if notes:
        with open(f"{note_title}.txt", "w") as file:
            file.write("\n".join(notes) + "\n")
            print("Notes saved.")
            speak("Notes saved.")
    else:
        print("No notes recorded.")
        speak("No notes recorded.")
    
    # Add a slight pause to allow the recognizer to close before further processing
    time.sleep(1)

def search_wikipedia(query):
    try:
        content = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        speak(content)
    except wikipedia.exceptions.PageError:
        speak("I couldn't find any information on Wikipedia.")
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]  # Limit the number of options to 5 for brevity
        speak(f"There are multiple results for {query}. Here are some options:")
        speak(", ".join(options))

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query}.")



def open_website(query):
    if "youtube" in query:
        webbrowser.open("https://www.youtube.com/")
        speak("Opening YouTube.")
    elif "gmail" in query:
        webbrowser.open("https://mail.google.com/")
        speak("Opening Gmail.")
    elif "google" in query:
        webbrowser.open("https://www.google.com/")
        speak("Opening Google.")
    elif "github" in query:
        webbrowser.open("https://github.com/")
        speak("Opening GitHub.")
    elif "stackoverflow" in query:
        webbrowser.open("https://stackoverflow.com/")
        speak("Opening Stack Overflow.")
    elif "amazon" in query:
        webbrowser.open("https://www.amazon.com/")
        speak("Opening Amazon.")
    elif "wikipedia" in query:
        webbrowser.open("https://www.wikipedia.org/")
        speak("Opening Wikipedia.")
    elif "reddit" in query:
        webbrowser.open("https://www.reddit.com/")
        speak("Opening Reddit.")
    elif "twitter" in query:
        webbrowser.open("https://twitter.com/")
        speak("Opening Twitter.")
    elif "facebook" in query:
        webbrowser.open("https://www.facebook.com/")
        speak("Opening Facebook.")
    elif "linkedin" in query:
        webbrowser.open("https://www.linkedin.com/")
        speak("Opening LinkedIn.")
    elif "instagram" in query:
        webbrowser.open("https://www.instagram.com/")
        speak("Opening Instagram.")
    elif "spotify" in query:
        webbrowser.open("https://www.spotify.com/")
        speak("Opening Spotify.")
    elif "netflix" in query:
        webbrowser.open("https://www.netflix.com/")
        speak("Opening Netflix.")
    elif "amazon prime video" in query:
        webbrowser.open("https://www.primevideo.com/")
        speak("Opening Amazon Prime Video.")
    elif "viggo" in query:
        webbrowser.open("link til vigo skole app")
        speak("Opening Viggo.")
    else:
        speak("Sorry, I don't know how to open that website.")

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data["setup"], joke_data["punchline"]
    else:
        return None, None
    
def tell_joke():
    joke_setup, joke_punchline = get_random_joke()
    if joke_setup and joke_punchline:
        speak(joke_setup)
        speak(joke_punchline)
    else:
        speak("Sorry, I couldn't fetch a joke at the moment. Please try again later.")

def play_music_youtube(query):
    if "music" in query:
        speak("Sure! What music would you like to listen to?")
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)
        music_query = recognizer.recognize_google(audio, language='en').lower()
        search_query = "youtube.com/results?search_query=" + music_query.replace(" ", "+")
        webbrowser.open(search_query)
        speak(f"Here are the search results for {music_query} on YouTube.")
    else:
        speak("Sorry, I'm not sure what music you want me to play.")

def solve_math_question(question):
    try:
        # Extract the math expression from the question
        math_expression = question.replace("what is", "").strip()
        
        # Replace 'x' with '*' for proper multiplication syntax
        math_expression = math_expression.replace('x', '*')
        
        result = eval(math_expression)
        speak(f"The answer is {result}.")
    except Exception as e:
        speak("Sorry, I couldn't solve the math question.")

def open_food_website(website):
    if "wolt" in website:
        webbrowser.open("https://wolt.com/")
        speak("Opening Wolt. Enjoy your meal!")
    elif "just eat" in website:
        webbrowser.open("https://www.just-eat.com/")
        speak("Opening Just Eat. Enjoy your meal!")
    elif "rema" in website:
        webbrowser.open("https://shop.rema1000.dk")
        speak("Opening Rema. Enjoy your meal!")
    else:
        speak("Sorry, I didn't understand your choice. Please try again later.")

def order_food():
    supported_websites = ["wolt", "just eat", "rema"]
    website_aliases = {
        "wolt": ["wolf", "bold", "v", "wolt"],
        "just eat": ["just eat", "just it", "just"],
        "rema": ["rema", "vigo"],
    }
    
    speak("Sure! Where would you like to order from? You can choose Wolt, Just Eat, or Rema Vigo.")
    
    while True:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

        website_choice = recognizer.recognize_google(audio, language='da').lower()
        print("User:", website_choice)

        for website, aliases in website_aliases.items():
            if any(alias in website_choice for alias in aliases):
                chosen_website = website
                break
        else:
            chosen_website = None

        if chosen_website:
            break
        else:
            speak("Sorry, I didn't understand your choice. Please choose Wolt, Just Eat, or Rema Vigo.")

    speak(f"You chose {chosen_website}. Let me open the website for you.")
    open_food_website(chosen_website)

def respond_to_thank_you():
    responses = ["You're welcome!", "No problem!", "My pleasure!", "Anytime!"]
    speak(random.choice(responses))

def respond_to_hello():
    responses = ["Hello there! How can I assist you today?", "Hi! How can I help you?", "Hey! What can I do for you?", "Greetings! What can I assist you with?", "Hello! I'm here to help. What do you need?", "Hi there! What can I do to make your day better?", "Hey! How can I be of service to you?", "Hi! Let's chat. What can I answer or find for you?", "Greetings! I'm ready to assist. What can i do for you?"]
    speak(random.choice(responses))

def get_pickup_line():
    pickup_lines = [
        "Are you a robot? Because you've got all the right algorithms to steal my heart.",
        "Are you made of metal and circuits? Because you've got me wired up for you.",
        "Is your name R2-D2? Because you've got a cute little beep-beep in my heart.",
        "I must be a robot, because every time I see you, my gears start turning.",
        "You must be a robot, because you've got the perfect blend of artificial intelligence and charm.",
        "Is your name WALL-E? Because you've cleaned up all the space in my mind.",
        "Are you a robot from the future? Because you're giving me a glimpse of what love will be like.",
        "If I were a robot, I'd have a heart filled with zeros and ones for you.",
        "I must be in a sci-fi movie, because meeting you is like a dream from the future.",
        "Is your name Alexa? Because you've got me saying 'yes' to everything you do.",
    ]
    return random.choice(pickup_lines)

def translate_text():
    translator = Translator()

    speak("Which language should I translate the text to?")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    target_language = recognizer.recognize_google(audio, language='en').lower()

    speak("What is the text?")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    text_to_translate = recognizer.recognize_google(audio, language='en')

    try:
        translated_text = translator.translate(text_to_translate, dest=target_language)
        print(f"Original Text: {text_to_translate}")
        print(f"Translated Text: {translated_text.text}")
        speak(f"The translated text is: {translated_text.text}")
    except Exception as e:
        speak("Sorry, I couldn't perform the translation at the moment. Please try again later.")

def set_timer():
    speak("Sure! For how long would you like to set the timer?")
    while True:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

        timer_query = recognizer.recognize_google(audio, language='en').lower()
        print("User:", timer_query)

        if "seconds" in timer_query:
            seconds = int(timer_query.split("seconds")[0].strip())
            time.sleep(seconds)
            speak(f"Timer for {seconds} seconds has ended.")
            break
        elif "minutes" in timer_query:
            minutes = int(timer_query.split("minutes")[0].strip())
            time.sleep(minutes * 60)
            speak(f"Timer for {minutes} minutes has ended.")
            break
        elif "hours" in timer_query:
            hours = int(timer_query.split("hours")[0].strip())
            time.sleep(hours * 3600)
            speak(f"Timer for {hours} hours has ended.")
            break
        else:
            speak("Sorry, I couldn't understand the timer duration. Please try again.")

def chatbot():
    activation_phrase = ["hello mixie", "hi mixie", "hey mixie", "hello missy", "hi missy", "hey missy", "hello miss you", "i miss you", "we'll miss you"]
    activated = False

    while True:  # Outer loop to keep the chatbot running indefinitely
        while not activated:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening for wakeup...")
                recognizer.pause_threshold = 1
                audio = recognizer.listen(source)

            try:
                user_input = recognizer.recognize_google(audio, language='en').lower()
                print("User:", user_input)

                if any(phrase in user_input for phrase in activation_phrase):
                    activated = True
                    speak("Hello! How can I assist you today?")
                else:
                    speak("Waiting for wakeup...")

            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass

        while activated:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.pause_threshold = 1
                audio = recognizer.listen(source)

            try:
                query = recognizer.recognize_google(audio, language='en').lower()
                print("User:", query)

                if any(word in query for word in ["turn off", "stop", "exit", "quit", "goodbye", "good bye", "bye"]):
                    speak("Turning off. Goodbye!")
                    activated = False  # Deactivate the chatbot and go back to waiting for wake-up
                elif "note" in query:
                    take_notes()
                elif any(word in query for word in ["what is the time", "what is the clock"]):
                    get_time()
                elif "date" in query and "in" not in query:
                    get_date()
                elif "tomorrow" in query and ("date" in query or "day" in query):
                    get_tomorrow_date()
                elif "date in" in query:
                    get_date_in_days(query)
                elif "search" in query:
                    query = query.replace("search", "").strip()
                    search_web(query)
                elif "weather" in query:
                    get_weather_info()
                elif "open" in query:
                    open_website(query)
                elif "joke" in query:
                    tell_joke()
                elif "music" in query:
                    play_music_youtube(query)
                elif "translate" in query and "text" in query:
                    translate_text()
                elif any(word in query for word in ["pickup line", "pick up line"]):
                    speak(get_pickup_line())
                elif "what is" in query:
                    solve_math_question(query)
                elif "i'm hungry" in query or "some food" in query or "i am hungry" in query:
                    order_food()
                elif any(word in query for word in ["set timer", "set a timer", "start a timer", "start timer"]):
                    set_timer()
                elif any(greeting in query for greeting in ["thank you", "thanks"]):
                    respond_to_thank_you()
                elif any(greeting in query for greeting in ["hello", "hi", "hey", "hi missy", "i miss you", "hello missy", "abc", "play"]):
                    respond_to_hello()
                elif any(word in query for word in ["shutdown the program", "shut down the program"]):
                    speak("Shutting down. Goodbye!")
                    sys.exit()  # Exit the script
                else:
                    search_wikipedia(query)

            except sr.UnknownValueError:
                print("Sorry, I couldn't understand you. Could you please repeat?")
                speak("Sorry, I couldn't understand you. Could you please repeat?")
            except sr.RequestError:
                print("Sorry, I'm having trouble processing your request. Please try again later.")
                speak("Sorry, I'm having trouble processing your request. Please try again later.")

if __name__ == "__main__":
    chatbot()
    
# Chatbot made by Clever Coding Coder
# https://www.fiverr.com/wellwithworld?up_rollout=true
# https://github.com/clevercodingcoder/