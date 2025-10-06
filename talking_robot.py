"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import pyttsx3
engine = pyttsx3.init()
import speech_recognition as sr
import speech_recognition as sr

import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyCV4QPs5zokQXJk9tw4uR9yH28f7acdCfk")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "hi",
      ],
    },
  ]
)

#response = chat_session.send_message("limit to 10 words/nexplane about wifi")

#print(response.text)

#engine.say(response.text)
#print("speaking...")
#engine.runAndWait()
#print("completed...")

recognizer = sr.Recognizer()

# Capture audio input from the microphone
with sr.Microphone() as source:
 print("Speak something...")
 audio_data = recognizer.listen(source)

# Perform speech recognition using Google Web Speech API
try:
 text = recognizer.recognize_google(audio_data)
 print("You said:", text)
 response = chat_session.send_message(f"Limit to 100 words \n {text}")
 engine.say(response.text)
 print("speaking...")
 engine.runAndWait()
 print("completed...")
except sr.UnknownValueError:
 print("Sorry, could not understand audio.")
except sr.RequestError as e:
 print("Error: Could not request results from Google Speech Recognition service;")