import speech_recognition as sr
import pyttsx3
from googlesearch import search
import datetime
#import pyaudio

# Initialize the speech recognition and synthesis engines
recognizer = sr.Recognizer()
synthesizer = pyttsx3.init()

def process_user_speech(user_speech):
    query = user_speech.lower()
    results = list(search(query, num_results=1))
    if results:
        response = results[0]
        # Perform further processing or return the response
        return response
    else:
        return "Sorry, I couldn't find any relevant information."

# Example usage
user_speech = "How does photosynthesis work?"
response = process_user_speech(user_speech)
print(response)


# Main loop to listen for user speech
while True:
    # Listen for user speech
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Recognize user speech
        user_speech = recognizer.recognize_google(audio)
        print("User:", user_speech)

        # Process user speech and generate a response
        response = process_user_speech(user_speech)
        print("Assistant:", response)

        # Synthesize and speak the response
        synthesizer.say(response)
        synthesizer.runAndWait()

        # Check for exit command
        if response == "Goodbye!":
            break

    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        print("Sorry, an error occurred while processing your speech:", str(e))
