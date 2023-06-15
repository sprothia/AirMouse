from flask import Flask, render_template, redirect, url_for
import subprocess
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def run_script():
    subprocess.run([f"{sys.executable}", 'MacControl.py'])
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=False, port=5000)

