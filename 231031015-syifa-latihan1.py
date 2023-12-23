nilai = int(input("Masukkan nilai (0-100): "))

if 0 <= nilai <= 100:
    batas_lulus = 65
    if nilai > batas_lulus:
        print('Selamat,kamu telah lulus!')
    else:
        print('Maaf,Kamu tidak lulus.')
else:
    print('Masukan nilai di luar rentang yang diizinkan (0-100).')
 

