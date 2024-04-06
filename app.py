import json
from flask import Flask, request, redirect
from flask_cors import CORS
from skimage import io
import cv2

import imageProcess

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
    
    # If the client does not select a file, the browser submits an
    # empty file without a filename.
    if file and file.filename == '' or not allowed_file(file.filename):
        return "file is invalid", 400    

    # read the image
    image = io.imread(file)
    
    # rotate the image if width > height
    if image.shape[1] > image.shape[0]:
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    
    nutrition_label, success = imageProcess.processImage(image)
    
    if not success:
        response = app.response_class(
            response=json.dumps({"error": "Failed to process image"}),
            status=500,
            mimetype='application/json'
        )
        return response
    
    if nutrition_label is None:
        response = app.response_class(
            response=json.dumps({"error": "Nutrition Label Not Found"}),
            status=200,
            mimetype='application/json'
        )
        return response
    
    # set response content type to json
    response = app.response_class(
        response=json.dumps(nutrition_label.toDict()),
        status=200,
        mimetype='application/json'
    )
    return response