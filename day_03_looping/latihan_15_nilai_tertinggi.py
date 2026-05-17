"""
Tugas:

- User memasukkan jumlah mahasiswa.
- Setiap mahasiswa punya nama dan nilai.
- Program menampilkan mahasiswa dengan nilai tertinggi.
"""

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
nilai_tertinggi = 0
mahasiswa_terbaik = ""

for i in range (1,jumlah_mahasiswa + 1):
    
    print(f"\nMahasiswa ke-{i}")
    nama = input("Masukkan Nama: ")
    nilai = int(input("Masukkan nilai: "))
    
    if nilai > nilai_tertinggi:
        nilai_tertinggi = nilai
        mahasiswa_terbaik = nama
 
print(f"\nNilai tertinggi: {nilai_tertinggi}")
print(f"Nama terbaik: {nama}")     
