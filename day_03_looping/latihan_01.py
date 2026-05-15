# Materi for
for i in range(1,6): #menghitung angka dari 1 sampe sebelum 6
    print(f"Belajar python hari ke- {i}") 
    
# loop untuk menghitung total
total = 0

for i in range (1,6):
    nilai = input(f"Masukkan nilai ke-{i}: ")
    total = total + nilai
    
    print(f"total nilainya adalah{total} ")

# menghitung rata-rata
total = 0
jumlah_data = 5

for i in range (1,jumlah_data + 1):
    nilai = int(input(f"Masukkan nilai ke-{i}: "))
    total = total + nilai
    
rata_rata = total / jumlah_data

print(f"Total nilai : {total}")
print(f"Rata-rata nilai : {rata_rata}")

# while
# while akan terus berjalan selama kondisinya benar
angka = 1

while angka <= 5:
    print(f"Angka: {angka}")
    angka = angka + 1
    
# break
# break dipakai untuk menghentikan loop
while True:
    password = input("Masukkan password: ")
    
    if password == "python123":
        print("Login berhasil")
        break
    else:
        print("Password salah, coba lagi")
        
# continue
# continue dipakai untuk melewati satu putaran loop

for angka in range (1,6):
    if angka == 3:
        continue
    
    print(angka)
    
    