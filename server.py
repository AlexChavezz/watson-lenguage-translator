# from machinetranslation import translator
from flask import Flask
import translator_package

app = Flask("Web Translator")

@app.route("/englishToFrench", methods=["POST"])
def englishToFrench():
    return translator_package.translator.englishToFrench()

@app.route("/frenchToEnglish", methods=["POST"])
def frenchToEnglish():
    return translator_package.translator.frenchToEnglish()

@app.route("/englishToSpanish", methods=["POST"])
def englishToSpanish():
     return translator_package.translator.englishToSpanish()
    
@app.route("/")
def renderIndexPage():
     return translator_package.translator.renderIndexPage()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)