nama = input("Masukkan nama: ")
jurusan = input("Masukkan jurusan: ")
semester = int(input("Masukkan semester: "))
umur = int(input("Masukkan umur: "))
target = input("Masukkan target belajar: ")
skill = input("Masukkan skill yang sudah di miliki: ")

tahun_lahir = 2026 - umur

print("\n=== PROFIL BELAJAR PYTHON ===")

print(f"Halo, nama saya {nama}.")
print(f"Saya adalah mahasiswa jurusan {jurusan} semester {semester}.")
print(f"Umur saya {umur} tahun.")
print(f"Perkiraan tahun lahir saya adalah {tahun_lahir}.")
print(f"Target saya adalah menguasai python untuk {target}.")
print(f"Skill yang sudah saya miliki adalah {skill}.")