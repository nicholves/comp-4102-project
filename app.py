from flask import Flask, request, redirect
from skimage import io
import os

import imageProcess

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 25 * 1000 * 1000

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/', methods=['POST'])
def upload():
    # check if the post request has the file part
    if 'file' not in request.files:
        return "no file part", 400
    file = request.files['file']
    
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return "no selected file", 400
    
    if file and allowed_file(file.filename):
        image = io.imread(file)
        np_img = imageProcess.processImage(image)
        
        return str(np_img), 200