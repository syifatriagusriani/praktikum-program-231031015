# Input bilangan X dari pengguna
X = int(input("Masukkan bilangan X: "))

# Cek apakah bilangan X ganjil atau tidak
if X % 2 != 0:
    print(f"{X} adalah bilangan Ganjil")
else:
    print(f"{X} adalah bilangan Bukan Ganjil")

