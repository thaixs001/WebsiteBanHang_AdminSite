from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home_page():
    return render_template('home_page.html') 