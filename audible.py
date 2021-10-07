# Import necessary libraries
import pyttsx3
import requests
from bs4 import BeautifulSoup

# Main Engine Initialising
engine = pyttsx3.init('sapi5')
# Get Voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Audio Output
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Get Article URL
url = str(input("Paste article URL : \n"))
# Get text using requests
print("\n-------------------------------")
data = requests.get(url).text
# print(data) -> This outputs html markup

# Getting the soup {text} from the html page(data)
soup = BeautifulSoup(data,'html.parser')
article = soup.get_text()
print(article)

print(speak(article))
# If you want to save the speech as a audio file
engine.save_to_file(article, 'article.mp3')
engine.runAndWait()

print("Scroll Up To Audio Sync")
