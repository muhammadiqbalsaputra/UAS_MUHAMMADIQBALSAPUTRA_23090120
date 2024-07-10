import pandas as pd

nomerSiswa = ['1', '2', '3']
tabelMapel = ['Nama', 'Algoritma dan Struktur Data 2', 'Matematika Numerik']
nilaiSiswa = pd.DataFrame([
    ['Mahasiswa 1', 90, 80],
    ['Mahasiswa 2', 50, 60],
    ['Mahasiswa 3', 65, 70]
], index=nomerSiswa, columns=tabelMapel)

print(nilaiSiswa)
print('\n')

totalMatkul = nilaiSiswa.drop(columns=['Nama']).sum(axis=0)
print('======== Rata-Rata Setiap Mata Kuliah ========')
print(totalMatkul)
print('='*43)
print('\n')

totalNilaiMahasiswa = nilaiSiswa.drop(columns=['Nama']).sum(axis=1)
print('======== Rata-Rata Nilai Mahasiswa ========')
print(f'{totalNilaiMahasiswa}')
print('='*43)
print('\n')
