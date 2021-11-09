from flask import Flask, render_template,url_for,request,flash,redirect, jsonify
import os , io, sys
from werkzeug.utils import secure_filename
# from PIL import Image
# import numpy as np
# import time
# import base64
# import numpy as np

app = Flask(__name__, static_folder= '../flaskprototype/static')
app.secret_key = "123jslkdjfal"

UPLOAD_FOLDER = '../flaskprototype/static/uploads'


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 120 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('image.html')

@app.route('/', methods=['POST'])
def upload_image():
    #penanganan kasus jika salah input file
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']

    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))#saving
        flash('Image uploaded and being processed below')#pemrosesan
        # extension=filename.split(".")
        # extension=str(extension[1])
        # source = UPLOAD_FOLDER + "/" + filename
        # destination = '../flaskprototype/static/processed' + "/" + "hasil." + extension
        # os.rename(source,destination)

        #mengembalikan laman
        return render_template('image.html', filename=filename)

    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    print('display_image filename: ' + filename)
    return redirect(url_for('static',filename= 'uploads/' + filename), code=301)#uploading quality of image before

# @app.route('/download')
# def download_image(filename):
#     # tempat untuk memproses image
#     im = Image.open(UPLOAD_FOLDER + filename)
#     data = io.BytesIO()
#     im.save(data, "JPEG")
#     imgData = base64.b64encode(data.getvalue())

#     return redirect(url_for("image", img_data= imgData.decode('utf-8') ))

 
if __name__ == "__main__":
    app.run(debug=True)

