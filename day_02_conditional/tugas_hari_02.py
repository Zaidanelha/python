nama = input("Masukkan nama:")
nilai_tugas = int(input("Masukkan nilai: "))
nilai_uts = int(input("Masukkan nilai: "))
nilai_uas = int(input("Masukkan nilai: "))
jumlah_kehadiran = int(input("Masukkan jumlah kehadiran: "))

if nilai_tugas > 100 or nilai_uts > 100 or nilai_uas > 100:
    print("Input nilai tidak valid. Nilai tidak boleh lebih dari: 100")
else:
    nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4)

if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 75:
    grade = "B"
elif nilai_akhir >= 65:
    grade = "C"
elif nilai_akhir >= 55:
    grade = "D"
else:
    grade = "E"

print("=== HASIL KELULUSAN ===")
print(f"Nama mahasiswa   : {nama}")
print(f"Nilai akhir      : {nilai_akhir}")
print(f"Grade            : {grade}")

if nilai_akhir >= 75 and jumlah_kehadiran >= 12:
    print("Selamat anda lulus")
else:
    print("Maaf anda belum lulus")
    
    if nilai_akhir < 75:
        print("Alasan: nilai kurang dari 75")
        
    if jumlah_kehadiran < 12:
        print("Alasan: Kehadiran kurang dari 12")


