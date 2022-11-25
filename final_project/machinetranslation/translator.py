import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def englishToFrench(englishText):

    model_id = 'en-fr'
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3( version='2018-05-01', authenticator=authenticator)
    language_translator.set_service_url(url)
    translation = language_translator.translate(text=englishText, model_id=model_id)
    frencText = json.dumps(translation, indent=2, ensure_ascii=False)

    return frenchText

def frenchToEnglish(frenchText):

    model_id = 'fr-en'
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3( version='2018-05-01', authenticator=authenticator)
    language_translator.set_service_url(url)
    translation = language_translator.translate(text=FrenchText, model_id=model_id)
    englishText = json.dumps(translation, indent=2, ensure_ascii=False)
    
    return englishText