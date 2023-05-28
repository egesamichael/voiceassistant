import speech_recognition as sr
from googlesearch import search
import requests
from bs4 import BeautifulSoup

def get_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the relevant content from the web page
    # Modify this code based on the structure of the web page you are scraping
    article_content = soup.find('div', class_='article-content').text.strip()
    return article_content

def process_user_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        user_speech = recognizer.recognize_google(audio)
        print("User Speech:", user_speech)
        query = user_speech.lower()

        # Greetings and predefined responses
        if any(greeting in query for greeting in ["hello", "hi", "hey"]):
            response = "Hello! How can I assist you today?"
        elif "goodbye" in query:
            response = "Goodbye! Have a great day!"
        elif "thank you" in query:
            response = "You're welcome!"
        else:
            # Process user query using search engine
            results = list(search(query, num_results=1))
            if results:
                article_url = results[0]
                article_content = get_article_content(article_url)
                response = article_content
            else:
                response = "Sorry, I couldn't find any relevant information."

        return response
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that. Could you please repeat?"
    except sr.RequestError:
        return "Sorry, I'm currently experiencing some technical issues. Please try again later."

# Example usage
while True:
    response = process_user_speech()
    print("Assistant Response:", response)
