class restaurantwow:
    def __init__(self):
        self.pesanan = []
    
    def Enqueue(self,Masukanpesanan):
        self.pesanan.append(Masukanpesanan)
    
    def Dequeue(self):
        if len(self.pesanan):
            self.pesanan.pop(0)
        else:
            return None
    
    def tampilan(self):
        for index, NamaPesanan in enumerate(self):
            print(f'{index},{NamaPesanan}')