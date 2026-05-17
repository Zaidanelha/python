"""
Tugas:
Mirip latihan 15, tapi cari nilai yang paling rendah
"""

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

nilai_terendah = 101
mahasiswa_terburuk = ""

for i in range (1,jumlah_mahasiswa+1):
    
    print(f"\nMahasiswa ke-{i}")
    nama = input("Masukkan nama mahasiswa: ")
    nilai = int(input("Masukkan nilai: "))
    
    if nilai < nilai_terendah:
        nilai_terendah = nilai
        mahasiswa_terburuk = nama
        
print(f"\nNilai terendah: {nilai_terendah}")
print(f"Mahasiswa dengan nilai terendah: {mahasiswa_terburuk}")