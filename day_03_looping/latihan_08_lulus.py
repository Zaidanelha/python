"""
Tugas :
user memasukkan jumlah mahasiswa
untuk setiap mahasiswa, input nama dan nilai
program menghitung berapa yang lulus dan tidak lulus
"""

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa : "))

total_nilai = 0
total_lulus = 0
total_tidak_lulus = 0

for i in range (1,jumlah_mahasiswa + 1):
    print(f"\nMahasiswa ke- {i}")

    nama = input(f"Masukkan nama mahasiswa: ")
    nilai = int(input("Masukkan nilai : "))
    
    if nilai >= 75:
        status = "Lulus"
        total_lulus = total_lulus + 1
    else:
        status = "Tidak Lulus"
        total_tidak_lulus = total_tidak_lulus + 1
        
    print(f"Status : {status}")
    
print(f"\nJumlah lulus : {total_lulus}")
print(f"Jumlah tidak lulus : {total_tidak_lulus}")
    
    