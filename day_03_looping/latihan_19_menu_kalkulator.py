while True:
    print("\n=== KALKULATOR ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "5":
        print("Program selesai.")
        break

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == "1":
        hasil = angka1 + angka2
        print(f"Hasil: {hasil}")
    elif pilihan == "2":
        hasil = angka1 - angka2
        print(f"Hasil: {hasil}")
    elif pilihan == "3":
        hasil = angka1 * angka2
        print(f"Hasil: {hasil}")
    elif pilihan == "4":
        if angka2 == 0:
            print("Error: pembagian dengan nol tidak boleh.")
        else:
            hasil = angka1 / angka2
            print(f"Hasil: {hasil}")
    else:
        print("Menu tidak valid.")