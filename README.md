# SVD Image Compression Website
> Program kompresi gambar dengan memanfaatkan algoritma SVD dalam bentuk website lokal sederhana. Website mampu menerima file gambar beserta input tingkat kompresi gambar berupa jumlah nilai singular yang ingin digunakan. Website mampu menampilkan gambar input, output, runtime algoritma, dan persentase hasil kompresi gambar. File output hasil kompresi dapat diunduh melalui website. Program ini merupakan Tugas Besar untuk mata kuliah IF2123 Aljabar Linier dan Geometri.

## Daftar Anggota Kelompok
<table>
<tr><td colspan = 3 align = "center">KELOMPOK 51 SVDED</td></tr>
<tr><td>No.</td><td>Nama</td><td>NIM</td></tr>
<tr><td>1.</td><td>Flavia Beatrix Leoni A. S.</td><td>13520051</td></tr>
<tr><td>2.</td><td>Lyora Felicya</td><td>13520073</td></tr>
<tr><td>3.</td><td>Angelica Winasta Sinisuka</td><td>13520097</td></tr>
</table>

## Requirements
***Libraries***<br />
* Numpy<br />
* Pillow<br />

## How to Run
Make sure to have Python 3 installed already in your computer<br />

**For Windows**<br />
1. open cmd<br />
2. go inside src directory then type commands below :<br />
```
py -m venv env
env\Scripts\activate
pip install Flask
```
3. go inside flaskprototype folder by typing ```cd flaskprototype```, then run the command below :
```
set FLASK_APP=app.py
flask run
```
5. Copy the URL provided and run it in your browser. Make sure to have all the libraries listed up top.<br />
<br />

**For Debian/Ubuntu/MacOS**<br />
1. open terminal<br />
2. go inside src directory then type commands below :<br />
```
python3 -m venv env
source env/bin/activate
pip install Flask
```
3. go inside flaskprototype folder by typing ```cd flaskprototype```, then run the command below :
```
export FLASK_APP=app.py
flask run
```
4. Copy the URL provided and run it in your browser. Make sure to have all the libraries listed up top.<br />

## Cara Menggunakan Website
1. Masukkan banyaknya nilai singular yang ingin digunakan.
2. Pilih gambar untuk dikompres.
3. Tekan tombol Compress Now dan tunggu beberapa saat.
4. Hasil kompres akan muncul, untuk melihat detailnya silakan tekan tulisan image details.
5. Tekan tombol Download untuk mengunduh gambar ke komputer Anda.

## Screenshots
![Screenshot (2334)](https://user-images.githubusercontent.com/82488797/141688279-98ab95e7-d2ea-4ef2-9557-91cd3ea8dada.png)

![Screenshot (2336)](https://user-images.githubusercontent.com/82488797/141688721-5623a161-e87c-4136-a84f-d7808b3e603a.png)

## Project Structure
```
Algeo02-20051   
????????? src/flaskprototype                  # berisi source code dari program image compressor
???   ????????? __pycache__                     # berisi python3 bytecode yaang sudah dicompile dan dieksekusi
???   ????????? static                          # berisi file-file static
???   ???   ????????? css                         # berisi desain dari halaman 1 dan halaman 2
???   ???   ???   ????????? image.css               # template style image.html
???   ???   ???   ????????? image2.css              # template style image2.html
???   ???   ????????? processed                   # hasil gambar yang telah diproses
???   ???   ????????? uploads                     # hasil gambar yang diinput pengguna
???   ????????? templates                       # berisi layout website
???   ???   ????????? image.html                  # tampilan halaman pertama
???   ???   ????????? image2.html                 # tampilan halaman kedua
???   ????????? app.py                          # aplikasi flask
???   ????????? svd.py                          # file svd untuk mencompress image
????????? test                                # berisi images untuk dites
????????? doc                                 # berisi file laporan algeo  
????????? README.md
```