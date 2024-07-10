dataSiswa = []
while True:
    inputNIM = int(input('Masukan NIM : '))
    inputNama = input('Masukan Nama : ')
    dictSiswa = {'NIM':inputNIM,'Nama':inputNama}
    dataSiswa.append(dictSiswa)
    validasi = input('Apakah Ingin Menambah Lagi? ( YA / TIDAK ) : ').upper()
    if validasi == 'YA':
        continue
    else:
        print('=========== DATA MAHASISWA ===========')
        for index,dataMahasiswa in enumerate(dataSiswa):
            print(index+1,dataMahasiswa)
        print('===========Program Selesai===========')