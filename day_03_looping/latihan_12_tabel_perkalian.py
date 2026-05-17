"""
Tugas:
User memasukkan angka, lalu program menampilkan tabel perkalian 1 sampai 10
"""

jumlah_angka = int(input("Masukkan angka: "))

for i in range (1,11):
    perkalian = jumlah_angka * i
    
    print(f"{jumlah_angka} x {i} = {perkalian} ")