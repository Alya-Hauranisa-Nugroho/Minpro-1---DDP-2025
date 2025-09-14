# MINI PROJECT 1 Sistem Manajemen Pemesanan Bouquet Bunga
# Nama: Alya Hauranisa Nugroho
# NIM: 2509116005
# Kelas: Sistem Informasi 2025 (A)

#LISTTTT dan tuple
buket = ("Rosey Rose", "Majestic Lily", "Harmony of Pink Bloom", 
        "Rise and Shine", "Daisy Daze", "Beautiful in White", "Tulip in Your Eyes") #tuple paket bouquet

addon = ("Bunga Mawar", "Bunga Matahari", "Bunga Lily", 
        "Bunga Tulip", "Bunga Daisy", "Tidak Custom") #tuple custom add on bunga

kertas = ("Putih", "Hitam", "Coklat", "Pink") #tuple wrapping paper

status = ("Belum dikerjakan", "Dalam proses pembuatan", "Selesai") #tuple status orderan

order0 = ["Haur", "081333637409", "Harmony of Pink Bloom", "Bunga Mawar", "Putih", "Belum dikerjakan", "20-09-2025"] #list contoh orderan
order1 = ["Alya", "08123456789", "Rise and Shine", "Tidak Custom", "Coklat", "Dalam proses pembuatan", "25-09-2025"]
order2 = ["Kansa", "081347110004", "Tulip in Your Eyes", "Bunga Tulip", "Pink", "Belum dikerjakan", "22-09-2025"]
order3 = ["Gita", "081122334455", "Daisy Daze", "Tidak Custom", "Hitam", "Selesai", "18-09-2025"]
order4 = ["Arini", "086677889910", "Beautiful in White", "Bunga Mawar", "Putih", "Dalam proses pembuatan", "24-09-2025"]

orderan = [order0, order1, order2, order3, order4] #list orderan

#MENU UTAMA
print("----------------------------------------------------------------------------")
print("Hai floristku! Selamat datang di Sistem Manajemen Pemesanan Bouquet Bunga <3")
print("----------------------------------------------------------------------------")
print("\nPertama, pilih menu yang tersedia ya!")
print("1. Masukkan Orderan Baru")
print("2. Lihat Orderan")
print("3. Update Status Orderan")
print("4. Hapus Orderan")
print("5. Keluar >>>") 

#INPUT PILIHAN MENU
pilihan = int(input("Pilihan kamu: "))

#MENU1 MASUKKAN ORDERAN BARU
if pilihan == 1:
    namapemesan = input("\nNama pemesan: ")
    nohp = input("No HP: ")

    print("\nPilih paket bouquet bunga!")
    print("0 = Rosey Rose, \n1 = Majestic Lily, \n2 = Harmony of Pink Bloom, \n3 = Rise and Shine, "
        "\n4 = Daisy Daze, \n5 = Beautiful in White, \n6 = Tulip in Your Eyes")
    buketpilihan = int(input("Masukkan pilihan paket dari 0-6: "))
    if 0 <= buketpilihan <= 6:
        paket = buket[buketpilihan]
    else:
        print("Pilihan kamu tidak valid! :(")
        exit()

    print("\nApakah ada custom +add on bunga?")
    print("0 = Bunga Mawar, \n1 = Bunga Matahari, \n2 = Bunga Lily, "
        "\n3 = Bunga Tulip, \n4 = Bunga Daisy, \n5 = Tidak Custom")
    addonpilihan = int(input("Masukkan pilihan custom add on bunga dari 0-5: "))
    if 0 <= addonpilihan <= 5:
        custom = addon[addonpilihan]
    else:
        print("Pilihan kamu tidak valid! :(")
        exit()

    print("\nPilih warna wrapping paper!")
    print("0 = Putih, \n1 = Hitam, \n2 = Coklat, \n3 = Pink")
    kertaspilihan = int(input("Masukkan pilihan warna wrapping paper dari 0-3: "))
    if 0 <= kertaspilihan <= 3:
        wrap = kertas[kertaspilihan]
    else:
        print("Pilihan kamu tidak valid! :(")
        exit()

    deadline = input("Tanggal Pengambilan (DD-MM-YYYY): ")

    orderbaru = [namapemesan, nohp, paket, custom, wrap, status[0], deadline]
    orderan.append(orderbaru)
    print("\n-------------------------")
    print("Ringkasan Orderan Baru")
    print("-------------------------")
    print(f"Nama Pemesan: {namapemesan} \nNo HP: {nohp} \nPaket: {paket} \nAdd on: {custom} \nWrapping Paper: {wrap} \nStatus: {status[0]} \nTanggal Pengambilan: {deadline}")
    print("\n----------------------------")
    print("Daftar Orderan Kamu Sekarang:")
    print("----------------------------")
    print("Orderan 0 - ",orderan[0],"\nOrderan 1 - ",orderan[1],"\nOrderan 2 - ",orderan[2],"\nOrderan 3 - ",orderan[3],"\nOrderan 4 - ",orderan[4],"\nOrderan 5 - ",orderan[5])
    print("\nYAYYY!! Orderan baru berhasil ditambahkan, jangan lupa dikerjakan yaa! :D")

#MENU2 LIHAT ORDERAN
elif pilihan == 2:
    if len(orderan) == 0:
        print("\nBelum ada orderan, nih :(")
    else: 
        print("\nIni daftar orderan kamu:")
        print("Orderan 0 - ",orderan[0],"\nOrderan 1 - ",orderan[1],"\nOrderan 2 - ",orderan[2],"\nOrderan 3 - ",orderan[3],"\nOrderan 4 - ",orderan[4])

#MENU3 UPDATE STATUS ORDERAN
elif pilihan == 3:
    if len(orderan) == 0:
        print("\nOh noo, belum ada orderan buat diupdate :(")
    else:
        print("\nDaftar orderan kamu: ", "\nOrderan 0 - ",orderan[0],"\nOrderan 1 - ",orderan[1],"\nOrderan 2 - ",orderan[2],"\nOrderan 3 - ",orderan[3],"\nOrderan 4 - ",orderan[4])
        pilihan_update = int(input("\nMasukkan nomor orderan yang ingin kamu update: "))
        if 0 <= pilihan_update <= 4:
            print("\nUpdate status menjadi: \n0 = Belum dikerjakan, \n1 = Dalam proses pembuatan, \n2 = Selesai")
            statusbaru = int(input("Masukkan status baru dari 0-2: "))
        else:
            print("Pilihan kamu tidak valid! :(")
            exit()
        if 0 <= statusbaru <= 2:
            orderan[pilihan_update][5] = status[statusbaru]
            print("\nOrderan telah diupdate: ",orderan[pilihan_update])
            print("----------------------------")
            print("Daftar Orderan Kamu Sekarang:")
            print("----------------------------")
            print("Orderan 0 - ",orderan[0],"\nOrderan 1 - ",orderan[1],"\nOrderan 2 - ",orderan[2],"\nOrderan 3 - ",orderan[3],"\nOrderan 4 - ",orderan[4])
            print("YIPIII statusnya udah diupdate ya! :D")
        else:
            print("Pilihan kamu tidak valid! :(")
            exit()

#MENU4 HAPUS ORDERAN
elif pilihan == 4:
    if len(orderan) == 0:
        print("\nBelum ada orderan yang bisa dihapus :p")
    else:
        print("\nDaftar orderan kamu : ","\nOrderan 0 - ",orderan[0],"\nOrderan 1 - ",orderan[1],"\nOrderan 2 - ",orderan[2],"\nOrderan 3 - ",orderan[3],"\nOrderan 4 - ",orderan[4])
        delete = int(input("Hapus orderan nomor berapa?: "))
        if 0 <= delete <= 4:
            terhapus = orderan.pop(delete)
            print("\nTelah menghapus orderan: ",terhapus)
            print("----------------------------")
            print("Daftar Orderan Kamu Sekarang:")
            print("----------------------------")
            print("Orderan 0 - ",orderan[0],"\nOrderan 1 - ",orderan[1],"\nOrderan 2 - ",orderan[2],"\nOrderan 3 - ",orderan[3])
            print("Orderan berhasil dihapus ya! :D")
        else:
            print("Pilihan kamu tidak valid! :(")
            exit()

#MENU5 KELUAR
elif pilihan == 5:
    print("\nHEHEHE Terima kasih sudah menggunakan layanan kami <3")

#PILIHAN TIDAK VALID
else:
    print("Yahh... Menu yang kamu pilih tidak valid :(")