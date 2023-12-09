import numpy
import matplotlib

karyawan = int(input("masukkan jumlah karyawan : "))
jam = int(input("masukkan jam kerja karyawan : "))

b = int(input("masukkan banyak looping"))

for i in range(b):
    print('Employee {} worked for {}'. format (karyawan, jam))