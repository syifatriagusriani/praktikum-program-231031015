print ('Tugas 2\n')

print('Program Penjumlahan Waktu \n')
# Input waktu awal dari pengguna
waktu_awal = input("Masukkan waktu awal (JJ:MM): ")
jam_menit = waktu_awal.split(":")
jam_awal = int(jam_menit[0])
menit_awal = int(jam_menit[1])

# Input waktu tambahan dalam jam dan menit
jam_tambahan = int(input("Masukkan jam tambahan: "))
menit_tambahan = int(input("Masukkan menit tambahan: "))

# Menghitung waktu akhir
jam_akhir = (jam_awal + jam_tambahan + (menit_awal + menit_tambahan) // 60) % 24
menit_akhir = (menit_awal + menit_tambahan) % 60

# Mencetak hasil
print(f"Waktu sekarang menunjukkan Pukul {jam_akhir:02d}:{menit_akhir:02d}\n\n")


print('Program Selisih Waktu\n')
# Input waktu awal
waktu_awal = input("Masukkan waktu awal (JJ:MM): ")
jam, menit = map(int, waktu_awal.split(':'))

# Input jam dan menit yang akan dikurangkan
jam_kurang = int(input("Masukkan jumlah jam yang akan dikurangkan: "))
menit_kurang = int(input("Masukkan jumlah menit yang akan dikurangkan: "))

# Hitung waktu akhir
jam_akhir = (jam - jam_kurang - (menit_kurang // 60)) % 24
menit_akhir = (menit - (menit_kurang % 60)) % 60

# Cetak hasil
print(f"Waktu sekarang menunjukkan pukul {jam_akhir:02d}:{menit_akhir:02d}")

