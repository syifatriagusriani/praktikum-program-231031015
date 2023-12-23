nama = input("Masukkan besaran pendapatan: ")
pendapatan = int(nama)


if pendapatan < 1000000:
    persentase = 10
elif pendapatan >= 1000000 and pendapatan < 5000000:
    persentase = 15
else:
    persentase = 20

bonus = pendapatan * (persentase / 100)


total = pendapatan + bonus

print(f"Pendapatan awal: {pendapatan}")
print(f"Persentase bonus: {persentase}%")
print(f"Nilai bonus: {bonus}")
print(f"Total pendapatan: {total}")
