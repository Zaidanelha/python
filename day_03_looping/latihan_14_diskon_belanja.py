"""
Tugas:
Program menghitung total belanja dan diskon

Ketentuan:
- Jika total belanja >= 100000, diskon 10%
- Jika total belanja >= 250000, diskon 20%
- Jika total belanja < 100000, tidak dapat diskon
"""

total_belanja = int(input("Total belanja: "))

if total_belanja >= 250000:
    diskon = 0.2
elif total_belanja >= 100000:
    diskon = 0.1
else:
    diskon = 0
    
total_diskon = total_belanja * diskon
total_bayar = total_belanja - total_diskon

print(f"Total belanja: {total_belanja}")
print(f"Diskon: {diskon * 100:.0f}%")
print(f"Total bayar: Rp{total_bayar:.0f}")


