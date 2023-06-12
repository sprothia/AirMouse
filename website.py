from flask import Flask, render_template, redirect, url_for
import subprocess
        
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def run_script():
    subprocess.run(['python', 'MacControl.py'])
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

