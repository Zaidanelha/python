'''
Buat program Input Nilai Banyak Mahasiswa.

Fitur:
- User memasukkan jumlah mahasiswa.
- Program meminta nama dan nilai setiap mahasiswa.

Program menampilkan:
- nama mahasiswa
- nilai mahasiswa
- status lulus/tidak lulus

Setelah semua input selesai, tampilkan:
- total nilai
- rata-rata nilai
- jumlah mahasiswa lulus
- jumlah mahasiswa tidak lulus
'''

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

total_nilai = 0
jumlah_lulus = 0
jumlah_tidak_lulus = 0

print("=== INPUT DATA MAHASISWA ===")

for i in range (1, jumlah_mahasiswa + 1):
    print(f"Mahasiswa ke-{i}")
    
    nama = input("Masukkan nama: ")
    nilai = int(input("Masukkan nilai: "))
    
    total_nilai = total_nilai + 1

    if nilai >= 75:
        status = "Lulus"
        jumlah_lulus = jumlah_lulus + 1
    else:
        status = "Tidak Lulus"
        jumlah_tidak_lulus = jumlah_tidak_lulus + 1
    
    print(f"Nama mahasiswa : {nama}")
    print(f"Nilai Mahasiswa: {nilai}")
    print(f"Status Mahasiswa : {status}")
    
rata_rata = total_nilai / jumlah_mahasiswa

print("\n=== REKAP NILAI ===")
print(f"Total nilai : {total_nilai}")
print(f"Rata-rata nilai : {rata_rata}")
print(f"Jumlah mahasiswa yang lulus : {jumlah_lulus}")
print(f"Jumlah mahasiswa tidak lulus : {jumlah_tidak_lulus}")
    
    