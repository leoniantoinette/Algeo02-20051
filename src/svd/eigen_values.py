import numpy as np
from scipy.linalg import hessenberg

def eigen_values(A):
  ''' 
  menggunakan qr algorithm dengan shift
  misal Ak adalah matrix berukuran n x n
  lakukan QR decomposition pada Ak yang nilai pada elemen diagonal utamanya telah dikurangi dengan sk
  sk diambil dari elemen terakhir dari diagonal utama matrix
  Ak - sk * I = Qk * Rk
  lalu tambahkan nilai sk kembali pada matrix tersebut sehingga
  A(k+1) = Rk * Qk + sk * I
  lakukan langkah ini berulang kali hingga didapatkan matrix Ak yang menyerupai matrix diagonal
  '''
  # KAMUS
  # Ak  : matrix
  # n   : integer ukuran matrix
  # ALGORITMA
  Ak = hessenberg(A)
  n = Ak.shape[0]           # ukuran matriks yaitu n
  for i in range(100000):
    sk = Ak.item(n-1,n-1)   # ambil sk yaitu elemen terakhir dari matrix Ak
    # kalikan sk dengan matrix identitas berukuran n
    skI = sk * np.eye(n)
    # lakukan QR decomposition pada Ak - skI
    Q, R = np.linalg.qr(np.subtract(Ak, skI))
    # Ak yang baru merupakan perkalian dari Rk dengan Qk ditambah dengan skI
    Ak = np.add(R @ Q, skI)
  # nilai eigen dari A merupakan elemen diagonal dari Ak
  eigval = np.diag(Ak)
  return eigval

# untuk testing
A = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4, 8]])
print(eigen_values(A))