print("Selamat Datang !") #sambutan
def menu(): #pilihan menu, pake function biar bisa balik pas dipanggil lagi
    print("---Menu---")
    print("1.Daftar Kontak")
    print("2.Tambah Kontak")
    print("3.Keluar")
menu()
user = int(input("Pilih Menu : ")) #user masukan input
#valuestore opsi 1
kontak_1 = {
    "Nama"          : "Farhan",
    "No. Telepon"   :  "+628123456789",
}
kontak_2 = {
    "Nama"          : "Joko",
    "No. Telepon"   : "+628987654321"
}

daftar_kontak = []
daftar_kontak.append(kontak_1)
daftar_kontak.append(kontak_2)
while user !=3 :
    if user == 1:
        #data kontak awal 
        for kontak in daftar_kontak:
            print("Nama         : {}".format(kontak["Nama"]))
            print("No. Telepon  : {}".format(kontak["No. Telepon"]))
            
        menu()
        user = int(input("Pilih Menu : "))
    elif user == 2:
        #menambah input kontak
        kontak_3 = {}
        tambah_nama = input("Nama :")
        tambah_nomor = input("No. Telepon :")
        kontak_3["Nama"] = tambah_nama
        kontak_3["No. Telepon"] = tambah_nomor
        daftar_kontak.append(kontak_3)
       
        print("Kontak Berhasil Ditambahkan!")
        menu()
        user = int(input("Pilih Menu : "))
    else :
        print("Menu Tidak Tersedia!")
        menu()
        user = int(input("Pilih Menu : "))

print("Program selesai, sampai jumpa!")