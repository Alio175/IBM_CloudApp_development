from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/englishToFrench")
def englishToFrench():
    english_text = request.args.get("text")
    french_text = translator.englishToFrench(english_text)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    french_text = request.args.get("text")
    english_text = translator.frenchToEnglish(french_text)
    return english_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
