class restaurantow:
    def __init__(self):
        self.pesanan = []

    def Enqueue(self):
        masukanPesanan = input('Masukkan pesanan: ')
        self.pesanan.append(masukanPesanan)
        print(f'Order: {masukanPesanan} ditambahkan')

    def Dequeue(self):
        if len(self.pesanan) > 0:
            pesananDihapus = self.pesanan.pop(0)
            print(f'Order : {pesananDihapus} Dihapus')
        else:
            print('Antrian Tidak Ada')

    def tampilan(self):
        print('='*30)
        if len(self.pesanan) > 0:
            print('======= Daftar Antrian =======')
            for index,antrian in enumerate(self.pesanan):
                print(f'{index+1}. {antrian}')
        else:
            print('Antrian Tidak Ada')
        print('='*30)

