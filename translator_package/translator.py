from flask import render_template, request, jsonify
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()
authenticator = IAMAuthenticator(os.environ.get('API_KEY'))
language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
        )
language_translator.set_service_url(os.environ.get('URL'))

def englishToFrench():
    textToTranslate = request.get_json().get("textToTranslate")
    try:
        
        translation = language_translator.translate(
            text=textToTranslate,
            model_id='en-fr').get_result()
        return jsonify(translation['translations'])
    except Exception as e:
        print(e)
        return "Error"
    
def frenchToEnglish():
    textToTranslate = request.get_json().get("textToTranslate")
    try:
        translation = language_translator.translate(
            text=textToTranslate,
            model_id='fr-en').get_result()
        return jsonify(translation['translations'])
    except Exception as e:
        print(e)
        return "Error"
    
def englishToSpanish():
    textToTranslate = request.get_json().get("textToTranslate")
    try:
        translation = language_translator.translate(
            text=textToTranslate,
            model_id='en-es').get_result()
        return jsonify(translation['translations'])
    except Exception as e:
        print(e)
        return "Error"

def renderIndexPage():
    return render_template("index.html")