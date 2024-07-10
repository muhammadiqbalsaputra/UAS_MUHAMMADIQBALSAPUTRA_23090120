class Buah:
    def __init__(self, Nama, Warna, Rasa):
        self.__Nama = Nama
        self.__Warna = Warna
        self.__Rasa = Rasa

    def set_nama(self):
        return self.__Nama
    def set_warna(self):
        return self.__Warna
    def set_rasa(self):
        return self.__Rasa
    
    def information(self):
        return f'Buah: {self.set_nama()} \nWarna: {self.set_warna()} \nRasa: {self.__Rasa()}'

class Mangga:
    def __init__(self,Vitamin):
        self.__Vitamin = Vitamin

    def set_vitamin(self):
        return self.__Vitamin
    
    def info_vitamin(self):
        return f'Vitamin : {self.set_vitamin()}'


class BuahMangga(Buah, Mangga):
    def __init__(self, Nama,Warna,Rasa,Vitamin):
        Buah.__init__(self, Nama,Warna, Rasa,)
        Mangga.__init__(self,Vitamin)
    
    def info(self):
        return f'{self.information()}  {self.info_vitamin()} '

