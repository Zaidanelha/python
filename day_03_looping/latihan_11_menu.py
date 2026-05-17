while True:
    print("=== MENU ===")
    print("1. Sapa user")
    print("2. Hitung luas persegi")
    print("3. Keluar")
    
    pilih_menu = input("Pilih menu: ")
    
    if pilih_menu == "1":
        nama = input("Masukkan nama: ")
        print(f"Halo {nama}")
    elif pilih_menu == "2":
        sisi = int(input("Masukkan panjang sisi: "))
        luas_persegi = sisi * sisi
        print(f"Luas persegi adalah {luas_persegi}")
    elif pilih_menu == "3":
        print("Program berhenti")
        break
    else:
        print("menu tidak valid.")