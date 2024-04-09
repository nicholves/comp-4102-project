import json
from flask import Flask, request, redirect
from flask_cors import CORS
from skimage import io
import cv2

import components.imageProcess as imageProcess

app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 25 * 1000 * 1000
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# POST request to upload image
@app.route('/upload', methods=['POST'])
def upload():
    
    # check if the post request has the image
    if 'image' not in request.files:
        return "Image with name 'image' not included", 400
    file = request.files['image']
    
    if file and file.filename == '' or not allowed_file(file.filename):
        return "file is invalid", 400  # Check if the file is valid 

    image = io.imread(file)  # read the image file
    nutrition_label, success = imageProcess.processImage(image)  # process the image
    
    if not success:  # if the image processing failed
        response = app.response_class(
            response=json.dumps({"error": "Failed to process image"}),
            status=500,
            mimetype='application/json')
        return response
    
    if nutrition_label is None:  # if the nutrition label was not found
        response = app.response_class(
            response=json.dumps({"error": "Nutrition Label Not Found"}),
            status=200,
            mimetype='application/json')
        return response
    
    # return the nutrition label details as a JSON response
    response = app.response_class(
        response=json.dumps(nutrition_label),
        status=200,
        mimetype='application/json')
    
    return response