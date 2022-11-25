from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench/<textToTranslate>")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    machinetranslation.englishToFrench(textToTranslate)
    return "Translated text to French"

@app.route("/frenchToEnglish/<textToTranslate>")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    machinetranslation.frenchToEnglish(textToTranslate)
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
