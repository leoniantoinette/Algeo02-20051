import numpy as np
import time
import random

from numpy.linalg import det

# fungsi untuk mengecek apakah suatu matrix adalah matrix diagonal
def isDiagonal(A):
  # KAMUS
  # Ak  : matrix
  # n   : integer ukuran matrix

  # ALGORITMA
  Ac = np.copy(A)
  np.fill_diagonal(Ac, 0)
  return (Ac==0).all()

def eigen(A):
  ''' 
  Dengan Schur Factorization, suatu matrix A berukuran nxn dapat ditulis sebagai: 
    A = U T U*
  dimana U adalah unitary matrix dan T adalah matrix segitiga
  Karena U adalah unitary matrix maka U* = U*(-1) 
  Kalikan kedua ruas dengan U* di kiri dan U di kanan sehingga diperoleh
    U* A U = T
    (Uk*..U1*) A (U1..Uk) = T dengan k -> infinity
  Rearrange persamaan ini menjadi:
    A1 = U1* A U1
    A2 = U2* U1* A U1 U2 = U2* A1 U2
    dst
  sehingga Ak = T
  Diperoleh bahwa U1* A = R1, dimana R1 merupakan matrix diagonal atas
  Kalikan kedua ruas dengan U1 di kiri sehingga diperoleh
    A = U1 R1
  dimana U1 dan R1 dapat diperoleh dengan melakukan QR factorization
  Sehingga persamaan A1 = U1* A U1 dapat diubah menjadi
    A1 = R1 U1
  Oleh karena itu,
  Lakukan QR factorization secara terus menerus pada A, diperoleh matrix Q dan R
  dimana A yang baru merupakan hasil perkalian antara R dengan Q dari matrix A yang lama
  hingga diperoleh matrix A yang menyerupai matrix diagonal
  Elemen diagonal dari matrix A ini merupakan nilai eigen dari matrix A
  Lalu, hasil perkalian antara setiap Q yang diperoleh dari setiap QR factorization
  menghasilkan suatu matrix eigenvectors dari A
  '''
  # KAMUS
  # Ak, Q, R  : matrix
  # n         : integer ukuran matrix
  # eigvec    : matrix berisi vektor eigen dari matrix
  # eigval    : array berisi nilai eigen dari matrix

  # ALGORITMA
  Ak = np.copy(A)
  n = Ak.shape[0]           # ukuran matrix yaitu n
  # inisialisasi matrix eigvec dengan suatu matrix identitas berukuran n
  eigvec = np.eye(n)
  for i in range(500):
    # lakukan QR decomposition pada Ak
    Q, R = np.linalg.qr(Ak)
    Ak = R @ Q
    eigvec = eigvec @ Q
    if (isDiagonal(Ak)):
      break
  # nilai eigen dari A merupakan elemen diagonal dari Ak
  eigval = np.diag(Ak)
  return eigval, eigvec

def svd(A):
  # KAMUS
  # eigval1, eigval2  : array berisi nilai eigen dari matrix
  # U, V, VT, S       : matrix
  
  # ALGORITMA
  eigval1, U = eigen(A @ A.T)
  eigval2, V = eigen(A.T @ A)
  VT = V.T
  S = U.T @ A @ V
  return U, S, VT


# untuk testing
# np.set_printoptions(suppress=True)
# start_time = time.time()

# A = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4, 8]])

# u1,s1,v1= svd(A)
# u,s,v = np.linalg.svd(A)
# print("U")
# print(u1)
# print("U np")
# print(u)
# print("S")
# print(s1)
# print("S np")
# print(s)
# print("V")
# print(v1)
# print("V np")
# print(v)

# print(u1 @ s1 @ v1)
# print(u @ np.diag(s) @ v)

# final_time = time.time()
# print(final_time - start_time)