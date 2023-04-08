import os
from flask import render_template, jsonify
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
authenticator = IAMAuthenticator(os.environ.get('API_KEY'))
language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
        )
language_translator.set_service_url(os.environ.get('URL'))

def english_to_french(text_to_translate):
    print(text_to_translate)
    try:
        translation = language_translator.translate(
            text=text_to_translate,
            model_id='en-fr').get_result()
        return jsonify(translation['translations'])
    except Exception as error:
        print(error)
        return "Error"
    
def french_to_english(text_to_translate):
    try:
        translation = language_translator.translate(
            text=text_to_translate,
            model_id='fr-en').get_result()
        return jsonify(translation['translations'])
    except Exception as error:
        print(error)
        return "Error"
    
def english_to_spanish(text_to_translate):
    try:
        translation = language_translator.translate(
            text=text_to_translate,
            model_id='en-es').get_result()
        return jsonify(translation['translations'])
    except Exception as error:
        print(error)
        return "Error"

def render_index_page():
    return render_template("index.html")
