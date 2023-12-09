def input_barang(banyak_data, dict_supplier):
    for i in range(banyak_data):
        perbarang = {}
        kode_barang = input('Masukkan Kode Barang: ')
        nama_barang = input('Masukkan Nama Barang: ')
        harga = int(input('Masukkan Harga: '))
        jumlah = int(input('Masukkan Jumlah: '))
        perbarang['kode_barang'] = kode_barang
        perbarang['nama_barang'] = nama_barang
        perbarang['harga'] = harga
        perbarang['jumlah'] = jumlah

        dict_supplier['barang'].append(perbarang)

def input_supplier(banyak_data, dict_pelanggan):
    for i in range(banyak_data):
        persupplier = {}
        kode_supplier = input('Masukkan Supplier Code: ')
        nama_supplier = input('Masukkan Nama Supplier: ')
        status = input('Status ? ')
        persupplier['kode_supplier'] = kode_supplier
        persupplier['nama_supplier'] = nama_supplier
        persupplier['status'] = status.lower()

        if persupplier['status'] == 'tersedia':
            pass
        else:
            continue

        kota = input('Masukkan Kota: ')
        persupplier['kota'] = kota
        persupplier['barang'] = []

        jumlah_barang = int(input('Masukkan jumlah barang yang akan dimasukkan: '))

        input_barang(jumlah_barang, persupplier)
        
        dict_pelanggan['supplier'].append(persupplier)

def input_pelanggan(banyak_data, data_pelanggan):
    for i in range(banyak_data):
        perpelanggan = {}
        kode_pelanggan = input('Masukkan Kode Pelanggan: ')
        nama_pelanggan = input('Masukkan Nama Pelanggan: ')
        alamat = input('Masukkan Alamat: ')
        perpelanggan['kode_pelanggan'] = kode_pelanggan
        perpelanggan['nama_pelanggan'] = nama_pelanggan
        perpelanggan['alamat'] = alamat
        perpelanggan['supplier'] = []

        jumlah_supplier = int(input('Masukkan jumlah supplier yang akan dimasukkan: '))

        input_supplier(jumlah_supplier, perpelanggan)

        data_pelanggan.append(perpelanggan)

list_pelanggan = []

jumlah_pelanggan = int(input('Masukkan jumlah pelanggan yang akan dimasukkan: '))

input_pelanggan(jumlah_pelanggan, list_pelanggan)

print()

pelanggan_barang_terbanyak = {
    'kode_pelanggan': list_pelanggan[0]['kode_pelanggan'],
    'nama_pelanggan': list_pelanggan[0]['nama_pelanggan'],
    'jumlah_barang': 0
}

pelanggan_transaksi_terbesar = {
    'kode_pelanggan': list_pelanggan[0]['kode_pelanggan'],
    'nama_pelanggan': list_pelanggan[0]['nama_pelanggan'],
    'total_transaksi': 0
}

print('Data Pelanggan:')
for perpelanggan in list_pelanggan:
    jumlah_barang = 0
    total_transaksi = 0
    print(f"Kode Pelanggan: {perpelanggan['kode_pelanggan']}")
    print(f"Nama Pelanggan: {perpelanggan['nama_pelanggan']}")
    print(f"Alamat: {perpelanggan['alamat']}")

    print('Supplier yang disediakan:')
    for persupplier in perpelanggan['supplier']:
        print(f"Supplier Code: {persupplier['kode_supplier']}")
        print(f"Nama Supplier: {persupplier['nama_supplier']}")
        print(f"Status: {persupplier['status']}")

        if persupplier['status'] == 'tersedia':
            pass
        else:
            continue

        print(f"Kota: {persupplier['kota']}")

        print('Barang yang dibeli:')
        for perbarang in persupplier['barang']:
            jumlah_barang = jumlah_barang + perbarang['jumlah']
            total_harga = perbarang['harga'] * perbarang['jumlah']
            total_transaksi = total_transaksi + total_harga
            print(f"Kode Barang: {perbarang['kode_barang']}")
            print(f"Nama Barang: {perbarang['nama_barang']}")
            print(f"Harga: {perbarang['harga']}")
            print(f"Jumlah: {perbarang['jumlah']}")

    if jumlah_barang>pelanggan_barang_terbanyak['jumlah_barang']:
        pelanggan_barang_terbanyak['kode_pelanggan'] = perpelanggan['kode_pelanggan']
        pelanggan_barang_terbanyak['nama_pelanggan'] = perpelanggan['nama_pelanggan']
        pelanggan_barang_terbanyak['jumlah_barang'] = jumlah_barang

    if total_transaksi>pelanggan_transaksi_terbesar['total_transaksi']:
        pelanggan_transaksi_terbesar['kode_pelanggan'] = perpelanggan['kode_pelanggan']
        pelanggan_transaksi_terbesar['nama_pelanggan'] = perpelanggan['nama_pelanggan']
        pelanggan_transaksi_terbesar['total_transaksi'] = total_transaksi


print()
print('Pelanggan dengan jumlah barang terbanyak:')
print(f"Kode Pelanggan: {pelanggan_barang_terbanyak['kode_pelanggan']}")
print(f"Nama Pelanggan: {pelanggan_barang_terbanyak['nama_pelanggan']}")
print(f"Jumlah Barang: {pelanggan_barang_terbanyak['jumlah_barang']}")

print()
print('Pelanggan dengan transaksi terbesar:')
print(f"Kode Pelanggan: {pelanggan_transaksi_terbesar['kode_pelanggan']}")
print(f"Nama Pelanggan: {pelanggan_transaksi_terbesar['nama_pelanggan']}")
print(f"Total Transaksi: {pelanggan_transaksi_terbesar['total_transaksi']}")

