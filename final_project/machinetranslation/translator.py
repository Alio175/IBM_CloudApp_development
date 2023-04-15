
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#instiating IBM watson language translator

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    if not englishText:
        return "Please enter a valid text"
    translator = language_translator.translate(text=englishText,
     source='en',
      target='fr'
      ).get_result()
    frenchText = translator['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    if not frenchText:
        return "Please enter a valid text"
    translator = language_translator.translate(text=frenchText, source='fr', target='en').get_result()
    englishText = translator['translations'][0]['translation']
    return englishText
while True:
    text = input("Enter 1 for English to French translation and 2 for French to English(q to exit): ")
    if text == "1":
        englishText = input("Enter the English text to translate: ")
        print('French',englishToFrench(englishText))
    elif text == "2":
        frenchText = input("Enter the French text to translate: ")
        print('English:',frenchToEnglish(frenchText))
    elif text == "q":
        break  
    else:      
        print("Please enter a valid input")