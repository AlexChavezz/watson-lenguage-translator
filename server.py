# from machinetranslation import translator
from flask import Flask, request
import translator_package

app = Flask("Web Translator")

@app.route("/englishToFrench", methods=["POST"])
def englishToFrench():
    text_to_translate = request.get_json().get("textToTranslate")
    return translator_package.translator.english_to_french(text_to_translate)

@app.route("/frenchToEnglish", methods=["POST"])
def frenchToEnglish():
    text_to_translate = request.get_json().get("textToTranslate")
    return translator_package.translator.french_to_english(text_to_translate)

@app.route("/englishToSpanish", methods=["POST"])
def englishToSpanish():
    text_to_translate = request.get_json().get("textToTranslate")
    return translator_package.translator.english_to_spanish(text_to_translate)
    
@app.route("/")
def renderIndexPage():
    return translator_package.translator.render_index_page()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
