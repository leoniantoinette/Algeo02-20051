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
3. Tekan tombol compress dan tunggu beberapa saat.
4. Hasil kompres akan muncul, untuk melihat detailnya silakan tekan tulisan image details.
5. Tekan tombol download untuk mengunduh gambar ke komputer Anda.
