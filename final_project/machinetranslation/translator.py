import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('5qXyp_RD9UWx95q2tOtVtO23kI0tpOjF8nxj3Z1k_jnd')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/b0428e7c-ad61-45d5-a032-01c7a1c52e76')

def english_to_french(english_text):
    """
    Translates English to French
    """
    translation = language_translator.translate(
    text= english_text,
    model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translates French to English
    """
    translation = language_translator.translate(
    text= french_text,
    model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text