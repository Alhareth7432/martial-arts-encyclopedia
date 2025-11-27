from flask import Flask, render_template
import json

app = Flask(__name__)

# Load martial arts data
with open('data/styles.json', 'r', encoding='utf-8') as f:
    styles = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/styles')
def all_styles():
    return render_template('styles.html', styles=styles)

@app.route('/style/<id>')
def style_detail(id):
    style = next((s for s in styles if s['id'] == id), None)
    if style is None:
        return render_template('404.html'), 404
    return render_template('style_detail.html', style=style)

if __name__ == '__main__':
    app.run(debug=True)
