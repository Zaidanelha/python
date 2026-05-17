"""
Tugas:
Buat program login sederhana.

Ketentuan:
1. username benar : admin
2. password benar : python123
3. user diberi kesempatan login maksimal 3 kali
"""

username_benar = "admin"
password_benar = "python123"

for i in range(1,4):
    print(f"Percobaan ke-{i}")
    
    username = input("username: ")
    password = input("password: ")
    
    if username == username_benar and password == password_benar:
        print("Login berhasil")
        break
    else:
        print("Login gagal")
        
    if i == 3:
        print("Akun diblokir sementara")