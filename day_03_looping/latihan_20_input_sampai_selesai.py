total = 0
jumlah_data = 0

while True:
    input_nilai = input("Masukkan nilai atau ketik selesai: ")

    if input_nilai == "selesai":
        break

    nilai = float(input_nilai)

    total = total + nilai
    jumlah_data = jumlah_data + 1

if jumlah_data > 0:
    rata_rata = total / jumlah_data

    print(f"Total nilai: {total}")
    print(f"Jumlah data: {jumlah_data}")
    print(f"Rata-rata: {rata_rata:.2f}")
else:
    print("Tidak ada data nilai.")