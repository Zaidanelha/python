nilai = 80

# if
if nilai >= 75:
    print("Lulus")

# Jika nilai lebih besar atau sama dengan 75, jalankan kode dibawahnya (lulus)

# if else
nilai = int(input("Masukkan nilai:"))

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak lulus")
    
# if elif else
nilai = int(input("Masukkan nilai:"))
    
if nilai >= 85:
    grade = "A"
elif nilai >= 75:
    grade = "B"
elif nilai >= 65:
    grade = "C"
elif nilai >= 50:
    grade = "D"
else:
    grade = "E"
        
print(f"Grade kamu adalah {grade}")
        

# Operator Perbandingan
# == sama dengan
# != tidak sama dengan
# > lebih besar
# < lebih kecil
# >= lebih besar sama dengan
# <= lebih kecil sama dengan

# Operator Logika
# 1. and
# semua kondisi harus benar
umur = int(input("Masukkan umur:"))
punya_ktp = input("Punya ktp? (ya/tidak): ")

if umur >= 17 and punya_ktp == "ya":
    print("Boleh membuat SIM")
else:
    print("Belum boleh membuat SIM")
    
# 2. or
## salah satu kondisi benar sudah cukup
role = input("Masukkan role anda: ")

if role == "admin" or role == "owner":
    print("Boleh masuk dashboard")
else:
    print("Akses ditolak")
    
# not
# membalik kondisi
aktif = False

if not aktif:
    print("Akun tidak aktif")
    
    