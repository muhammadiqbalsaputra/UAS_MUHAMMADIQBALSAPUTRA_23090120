from modulSoal_3 import restaurantow

pesanan = restaurantow()
print('===Selamat Datang Di Restauran Iqbal===')
while True:

    print('1. Masukan Antrian')
    print('2. Antrian Selanjutnya')
    print('3. Tampilkan')
    print('4. Selesai')
    print('='*30)
    masukanPilihan = input('Masukan Pilihan : ')
    if masukanPilihan == '1':
        pesanan.Enqueue()
    elif masukanPilihan == '2':
        pesanan.Dequeue()
    elif masukanPilihan == '3':
        pesanan.tampilan()
    else:
        print('Terimakasih Telah Mencoba')
        exit()
