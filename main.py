import time
from google import generativeai as genai
from configparser import ConfigParser
import speech_recognition as sr
import pyttsx3


config = ConfigParser()
config.read('credentials.ini')

api_key = config['API_KEY']['google_key']

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

speech = sr.Recognizer()
engine = pyttsx3.init()
try:
    i = 0
    while i == 0:
        with sr.Microphone() as source:
            print('Listening...')
            audio = speech.listen(source)
        text = speech.recognize_google(audio)
        print(f"You said: {text}")
        response = model.generate_content(text)
        print(response.text)
        engine.say(response.text)
        engine.runAndWait()
        if text == "exit":
            exit(0)
        time.sleep(1)

except sr.UnknownValueError:
    print("Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Error with the speech recognition service; {e}")
except Exception as e:
    print(f"An error occurred: {e}")
