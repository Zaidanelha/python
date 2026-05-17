"""
Tugas:

Buat program login.

Ketentuan:

- username benar: admin
- password benar: python123
- maksimal percobaan 3 kali
- kalau benar, tampilkan Login berhasil
- kalau salah 3 kali, tampilkan Akun diblokir sementara
"""
username_benar = "admin"
password_benar = 123

for percobaan in range (1,3+1):
    
    print(f"\nPercobaan ke-{i}")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username == username_benar and password == password_benar:
        print("Login berhasil")
    else:
        print("Login gagal")
        
    if percobaan == 3:
        print("\nAkun di blokir sementara")
    