import json
from flask import Flask, request, redirect
from flask_cors import CORS
from skimage import io

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

    # process the image
    image = io.imread(file)
    nutrition_label, success = imageProcess.processImage(image)
    
    if not success:
        return "Nutrition Label Invalid", 400
    
    if nutrition_label is None:
        return "Nutrition Label Not Found", 200
    
    # set response content type to json
    response = app.response_class(
        response=json.dumps(nutrition_label.toDict()),
        status=200,
        mimetype='application/json'
    )
    return response