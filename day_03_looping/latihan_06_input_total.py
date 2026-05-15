"""
Tugas:
Program meminta user memasukkan 5 angka, lalu menghitung totalnya
"""

total = 0
for i in range (1,5+1):
    angka = int(input(f"Masukkan angka ke-{i} : "))
    total = total + angka
    
print(f"Total angka : {total}")