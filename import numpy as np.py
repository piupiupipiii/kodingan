import numpy as np

def is_happy_number(n):
    # Fungsi untuk menghitung jumlah kuadrat dari digit-digit angka
    def calculate_sum_of_squares(num):
        digits = np.array(list(str(num)), dtype=int)
        return np.sum(digits**2)

    # Set untuk mendeteksi siklus
    seen_numbers = set()

    # Ulangi proses hingga mendapatkan angka 1 atau mendeteksi siklus
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = calculate_sum_of_squares(n)

    # Jika n adalah 1, itu adalah Happy Number
    if n == 1:
        return True
    else:
        return False

# Meminta input dari pengguna
n = int(input("Masukkan bilangan: "))

# Memeriksa apakah n adalah Happy Number
if is_happy_number(n):
    print(n, "adalah Happy Number.")
else:
    print(n, "bukan Happy Number.")