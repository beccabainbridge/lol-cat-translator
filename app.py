from flask import Flask, request, render_template
from lol_cat_translator import LolCatTranslator

app = Flask(__name__)

t = LolCatTranslator()

@app.route('/', methods=['GET', 'POST'])
def main():
    translated_text = None
    if request.method == 'POST':
        text = request.form['text']
        translated_text = t.translate_message(text)
    return render_template("index.html", translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
