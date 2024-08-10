from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = 'AIzaSyAVd-YvGHz6CPz8Jxi8lOlevxMfV4PVlAk'

def translate_text(text, target_lang):
    url = f"https://translation.googleapis.com/language/translate/v2"
    params = {
        'q': text,
        'target': target_lang,
        'key': API_KEY
    }
    response = requests.post(url, params=params)
    return response.json()['data']['translations'][0]['translatedText']

@app.route('/', methods=['GET', 'POST'])
def index():
    original_text = ""
    selected_language = "en"  # Default language
    translation = ""

    if request.method == 'POST':
        original_text = request.form['text']
        selected_language = request.form['language']
        translation = translate_text(original_text, selected_language)

    return render_template('index.html', original_text=original_text, selected_language=selected_language, translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
