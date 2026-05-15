"""
Tugas:
Program meminta user memasukkan 5 nilai, lalu menampilkan total dan rata-rata
"""
jumlah_data = 5
total = 0
for i in range (1,5+1):
    nilai = int(input(f"Masukkan nilai ke-{i} : "))
    total = total + nilai
    rata_rata = total / jumlah_data
    
print(f"Total : {total}")
print(f"Rata-rata : {rata_rata}")
    
