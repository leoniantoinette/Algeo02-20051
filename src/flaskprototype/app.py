from flask import Flask, render_template,url_for,request,flash,redirect, jsonify, send_file,send_from_directory
import os , io
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
import base64
import numpy as np
import time
from svd import svd

app = Flask(__name__, static_folder= '../flaskprototype/static')
app.secret_key = "123jslkdjfal"

UPLOAD_FOLDER = '../flaskprototype/static/uploads'


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 120 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

global k_value
global imgdata
global total_time
global originalSize
global compressedSize
global percent
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Membuka file Image dan pecah menjadi martriks r,g,b
def openImage(imagePath):
    originalImage = Image.open(imagePath)
    image = np.array(originalImage).astype(float)

    imageRed = image[:, :, 0]
    imageGreen = image[:, :, 1]
    imageBlue = image[:, :, 2]

    return [imageRed, imageGreen, imageBlue, originalImage]

#kompress setiap r,g,b
def compression(A,k):
    U_color, S_color, V_color = svd(A)
    imgCompressed = np.zeros((A.shape[0],A.shape[1]))
    imgReconstructed = U_color[:, 0:k] @ (S_color)[0:k,0:k] @ V_color[0:k,:]
    imgCompressed = np.clip(imgReconstructed,0,255).astype('uint8')
    return imgCompressed



@app.route('/')
def home():
    return render_template('image.html')

@app.route('/', methods=["POST", "GET"])
def uploads():

    #penanganan kasus jika salah input file
    k_value = request.form['k_value']
    if k_value != '':
        flag= True
        i = 0
        # mengecek kalau input user sudah benar
        # buat input  k value
        
        temp = [num for num in k_value]
        while (i <len(temp) and (flag)):
            if not(temp[i].isdigit()):
                flag = False
            i +=1
        
        if (flag):
            k_value = int(k_value)
        else:
            flash('Jumlah singular value harus bilangan bulat lebih dari nol')
            return redirect(url_for("uploads"))   
        
        if (flag) and (k_value > 0):

            #buat mengecek file kalau sudah benar dan rentang k value
            if ('file' not in request.files):
                flash('Wrong File Part')
                return redirect(url_for("uploads"))
            file = request.files['file']

            if (file.filename == '') :
                flash('No image selected for uploading')
                return redirect(url_for("uploads"))

            if (file and allowed_file(file.filename)):
                #saving file

                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))#saving
                
                return redirect(url_for("compressing", filename = filename, k_value=k_value))

            else:
                flash('Allowed image types are - png, jpg, jpeg')
                return redirect(url_for("uploads"))
        else:
            flash('Nilai singular value harus lebih dari nol')
            return redirect(url_for("uploads"))
    else:
        flash('Put in singular value')
        return redirect(url_for("uploads"))


@app.route('/compressed/<filename>/<k_value>', methods=['GET','POST'])
def compressing(filename, k_value):
    #penanganan kasus jika salah input file
    k_value = int(k_value)
    
    image = np.array(Image.open('static/uploads/' + filename))

    #perhitungan matematis original dan compression image
    row = image.shape[0]
    col = image.shape[1]

    
    originalSize = (row * col * 3)
    compressedSize = (k_value * (1 + row + col) * 3)


    ratio = (compressedSize/originalSize)
    percent = (round(ratio * 100, 2))


    print(percent)

    #comppressing image after uploaded inside uploads folder
    start_time = time.time()
    r,g,b, originalImage = openImage('./static/uploads/' + filename)
    
    
    k_value = int(k_value)
    
    
    r_compressed = compression(r,k_value)
    g_compressed = compression(g,k_value)
    b_compressed = compression(b,k_value)

    img_r = Image.fromarray(r_compressed, mode=None)
    img_g = Image.fromarray(g_compressed, mode=None)
    img_b = Image.fromarray(b_compressed, mode=None)

    
    compressedImage = Image.merge("RGB",(img_r,img_g,img_b))
    

    #Total waktu compression
    
    print(percent)

    #saving in binary to display and file to download
    # data = io.BytesIO()
    # compressedImage.save(data, "JPEG")

    #penamaan file yang baru buat simpan hasil compress
    # renewnamefile = filename.split(".")
    # renewnamefile = renewnamefile[0]

    #save file hasil image
    compressedImage.save('static/processed/compressed' + 'hasil' + '.jpeg')
    final_time = time.time()
    total_time = final_time - start_time
    # mengembalikan laman
    return render_template('image2.html', filename=filename, sizebfr=originalSize, times= str("%.2f" %total_time), sizeaftr=compressedSize,percent=percent)

@app.route('/download') 
def downloadimg():
    return send_from_directory(directory='static/processed',path ='compressedhasil.jpeg',as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

