from flask import Flask, render_template, request
import base64
import time

  
app = Flask(__name__, template_folder='templates')
  
@app.route("/")
@app.route('/index')
def index(): 
        return render_template('index.html')

@app.route('/evaluate', methods = ['POST'])
def evaluate():
        imgDataB64 = request.form['imageData']
        imgDataPNG = base64.b64decode(imgDataB64[22:])
        fileName = str(time.time()) + ".png"
        with open(fileName,"wb") as fo:
                fo.write(imgDataPNG)
        return render_template('result.html', data=imgDataB64)