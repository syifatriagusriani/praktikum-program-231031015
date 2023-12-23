import os
os.system('clear')


nim = ['2','3','1','0','3','1','0','1','5']
# nim2 = '231031015'
print(nim[1:3])
# print(nim2[1:3])

# akses item
print(f'item indeks 0: {nim[0]}')
print(f'item indeks 4: {nim[4]}')
print(f'item indeks terakhir: {nim[len(nim)-1]}')

# akses indeks negatif
print(f'item indeks terakhir: {nim[-1]}')
print(f'item indeks prtama: {nim[-len(nim)]}')
print(f'item indeks 6[-3]: {nim[-3]}')
print(f'item indeks 4[-5]: {nim[-5]}')
print(f'item indeks 7[-2]: {nim[-2]}')

# akses indeks batas 
print(f'item indeks 1,2,...: \n {nim[1:]}')
print(f'item indeks 3,4,...: \n {nim[3:]}')
print(f'item indeks 0,1,2,: \n {nim[:3]}')
print(f'item indeks 0,1,2,3: \n {nim[:4]}')
print(f'item indeks semua: \n {nim[:]}')
print(f'item indeks [:8]: \n {nim[:-1]}')
print(f'item indeks [:6]: \n {nim[:-3]}')

# pengirisan
print(f'item indeks 1,2 : \n {nim[1:3]}')
print(f'item indeks 2,3,4 : \n {nim[2:5]}')
print(f'item indeks kosong : \n {nim[3:3]}')
print(f'item indeks [8:8] kosong : \n {nim[-1:-1]}')
print(f'item indeks [1:8]: \n {nim[1:-1]}')
print(f'item indeks [2:7]: \n {nim[2:-2]}')

# Latihan List
print('Latihan list', '='*20)
data = ['Syifa Tri Ausriani',2023,'Aktif']
nilai = [90,89,93,97]

print('Nama: '+ data[0])
print('Angkatan:', data[1])
print('status: '+ data[2])

print(f'{data[0]} status kuliah: {data[2]}')
print(f'Data terbesar nilai adalah: {max(nilai)}')
print(f'Data terkecil nilai adalah: {max(nilai)}')
x_bar = sum(nilai)/len(nilai)
print(f'Rata-rata nilai adalah:{x_bar}')

# Latihan Tuple
print('Latihan tuple', '='*20)
data = ('Syifa Tri Agusriani',2023,'Aktif')
nilai = [90,89,93,97]

print(data[1])
print(data[-1])
print(data[1:-1])

print(f'Jumlah nilai mahasiswa adalah {len(nilai)}\n')
print(f'Data terbesar nilai adalah {max(nilai)}\n')
print(f'Data terkecil nilai adalah {min(nilai)}\n')
print(f'Rata-rata nilai adalah {sum(nilai)/len(nilai)}')

# Latihan Nested List
data = [['Syifa',2023,'Aktif'],
         [90,89,93,97],
         [20,22],
         ['S1-Reguler','Ganjil']]

matkul = ['Matkul1','Matkul2','Matkul3','Matkul4']
sks    = [2,3,3,2]
# Menambahkan matkul dan sks ke dalam data (di akhir)
data.append(matkul)
data.append(sks)
print(data)
# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f'Mata kuliah 1:{data[4][0]} dengan jumlah {data[5][0]} sks')
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print(f' Mata kuliah 2:{data[4][1]} dengan jumlah {data[5][1]} sks')
# Mata kuliah 3: Matkul3 dengan jumlah 3 sks
print(f' Mata kuliah 3:{data[4][2]} dengan jumlah {data[5][2]} sks')
# Mata kuliah 4: Matkul4 dengan jumlah 2 sks
print(f' Mata kuliah 4:{data[4][3]} dengan jumlah {data[5][3]} sks')

data[4].append('Matkul5')
data[5].append(2)
# Tambahkan 3 matkul dengan sks nya
data[4].append('Matkul6')
data[5].append(3)
data[4].append('Matkul7')
data[5].append(2)
data[4].append('Matkul8')
data[5].append(3)
print(data)

# Mata kuliah 5: Matkul5 dengan jumlah .. sks
print(f'Mata kuliah 5:{data[4][4]} dengan jumlah {data[5][4]} sks')
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f'Mata kuliah 6:{data[4][5]} dengan jumlah {data[5][5]} sks')
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f'Mata kuliah 7:{data[4][6]} dengan jumlah {data[5][6]} sks')
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f'Mata kuliah 8:{data[4][7]} dengan jumlah {data[5][7]} sks')

# Tambahkan 8 nilai masing-masing
data[1].append(95)
data[1].append(88)
data[1].append(96)
data[1].append(87)
print(data)

print(data[0][0])
print(data[-1][0])
print(data[2][0:])

# >> Tugas: Nama Mahasiswa Thomas dengan NIM: 600201014
print(f'Nama mahasiswa {data[0][0]} dengan NIM: {"".join(nim)}')

print(f'\nProgram pendidikan {data[0][0]}: {data[1][0]}\n')
print(f'Angakatan {data[0][1]}-{data[3][1]}\n')
print(f'Jumlah nilai {data[0][0]} : adalah : {len(data[1])}\n')
print(f'Data terbesar {data[0][0]} adalah : {max(data[1])}\n')
print(f'Data terkecil nilai adalah : {min(data[1])}\n')
print(f'Rata-rata nilai adalah : {sum(data[1])/len(data[1])}\n')



        





