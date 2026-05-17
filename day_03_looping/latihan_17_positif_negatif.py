"""
Tugas:
- User memasukkan 5 angka
- Program menghitung berapa angka positif, negatif, dan nol
"""

kuota = 5
status_positif = 0
status_negatif = 0
status_nol = 0

for i in range (1, kuota + 1):
    angka = int(input(f"Masukkan angka ke-{i}: "))
    
    if angka > 0:
        status_positif = status_positif + 1
    elif angka < 0:
        status_negatif = status_negatif + 1
    else:
        status_nol = status_nol + 1
        
print(f"Jumlah positif: {status_positif}")
print(f"Jumlah negatif: {status_negatif}")
print(f"Jumlah nol: {status_nol}")
