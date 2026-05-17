"""
Tugas:
User memasukkan jumlah barang.
Setiap barang punya nama dan harga.
Program menghitung total belanja.
"""

jumlah_barang = int(input("Masukkan jumlah barang: "))
total_belanja = 0

for i in range (1, jumlah_barang + 1):
    print(f"\nBarang ke-{i}")
    nama_barang = input("Nama barang: ")
    harga_barang = int(input("Harga barang: "))
    total_belanja = total_belanja + harga_barang
    
    print(f"Nama barang: {nama_barang}")
    print(f"Harga barang: {harga_barang}")
    
print(f"\nTotal belanja: Rp{total_belanja}")
    