"""
Tugas:
Program meminta user memasukkan nilai.
Kalau nilai kurang dari 0 atau lebih dari 100, user harus input ulang
"""
while True:
    nilai = int(input("Masukkan nilai: "))
    
    if nilai < 0 or nilai > 100:
        print("Nilai tidak valid. Masukkan 0 sampai 100.")
    else:
        print(f"Nilai valid: {nilai}")
        break