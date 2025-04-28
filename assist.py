import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import urllib.parse
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, there was an issue with the speech recognition service.")
            return ""
def open_youtube():
    try:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    except Exception:
        speak("Sorry, I couldn't open YouTube. Please check your internet connection.")

def open_google():
    try:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    except Exception:
        speak("Sorry, I couldn't open Google. Please check your internet connection.")


def search_google(query):
    try:
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        webbrowser.open(search_url)
        speak(f"Searching for {query} on Google")
    except Exception:
        speak("Sorry, I couldn't perform the search. Please check your internet connection.")

if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            if "open youtube" in command:
                open_youtube()
            elif "open google" in command:
                open_google()
            elif "exit" in command:
                speak("Goodbye!")
                break
            else:
                search_google(command)
