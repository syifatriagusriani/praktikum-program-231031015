correct_namapengguna = "sipa"
correct_katasandi = "syifa"

def login(nama_pengguna, pass_word):
    return nama_pengguna == correct_namapengguna and pass_word == correct_katasandi

attempts_left = 3

while attempts_left > 0:
    
    user_input = input("Masukkan nama anda: ")
    pass_input = input("Masukkan katasandi anda: ")

    if login(nama_pengguna=user_input, pass_word=pass_input):  # Corrected function call
        print("Selamat Anda Telah Login!")
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Gagal login. Sisa percobaan: {attempts_left}")
        else:
            print("Maaf, percobaan login habis. Akun anda tidak bisa login.")