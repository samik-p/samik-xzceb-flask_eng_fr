"""
This module uses Watson Language Translator to translate text from English to
French or from French to English.
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(english_text):
    """
    This function takes English text and translates it to French text
    """

    if english_text != '':
        result = language_translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()
        french_text = result['translations'][0]['translation']
    else:
        french_text = ''

    return french_text


def frenchToEnglish(french_text):
    """
    This function takes French text and translates it to English text
    """

    if french_text != '':
        result = language_translator.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()
        english_text = result['translations'][0]['translation']
    else:
        english_text = ''

    return english_text
