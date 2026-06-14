#sudah selesai

import json # modul json (JavaScript Object Notation)
import os #modul pembantu untuk cek apkah file sudah ada difolder atau belum

#proses pembacaan file (read)
FILE_NAMA = "database_keuangan_digital.json"
def data_total():
    #kalau sudah ada, dibuka dengan mode 'r' read
    with open(FILE_NAMA, "r") as file_uang:
        #sedot data dri file yg dikonversi ke list dn dictionary python
        riwayat_transaksi = json.load(file_uang)
        return riwayat_transaksi
#cek apakah file/notanya sudah pernah dibuat sebelumnya
if os.path.exists(FILE_NAMA):
    riwayat_transaksi = data_total()
    print("Berhasil memuat data riwayat dari laptop")
else:
    #kalau baru pertama kali dibuat filenya
    riwayat_transaksi=[]
    print("Belum ada riwayat keuangan kamu")

total_penghasilan = 0 #penghasilan?pengeluaran dimulai dari 0
total_pengeluaran = 0 #penghasilan?pengeluaran dimulai dari 0

for nota in riwayat_transaksi:
    if nota["Kategori"] == "penghasilan":
        total_penghasilan = nota["nominal"] + total_penghasilan
    elif nota["Kategori"] == "pengeluaran":
        total_pengeluaran = nota["nominal"] + total_pengeluaran
    elif nota == "dana_bersih":
        dana_bersih = total_penghasilan - total_pengeluaran

#menu tampilan utama dan while loop nya
while True:
    print("----Pencatat Keuangan Digital----")
    print("1. Tambah Nota Transaksi")
    print("2. Lihat Riwayat Transaksi")
    print("3. Keluar")
    pilihan = input("Pilih Menu yang di inginkan = ")

    #menu tampilan 1 dan perhitungannya
    if pilihan == "1":
        print("--Tambah Nota Transaksi--")

        #bentang try dan value eror agar aplikasi tetap berjalan dan tidak eror mati
        try:

        #proses input nominal uang
            uang = (input("\nMasukan uang kamu (Mohon masukan nominal berupa angka)= "))
        except ValueError:
            print("Gagal!! Mohon Masukan nominal uang yang benar dengan angka, bukan huruf!! Jangan memasukan Angka 0")
            continue
        if uang == 0:
            print("Mohon Masukan nominal uang yang benar dengan angka, bukan huruf!! Jangan memasukan Angka 0")
            break
        else: uang = int(uang)
        mata_uang = f"Rp {uang:,.0f}".replace(",",".")
        if uang > 0:
            print("uang kamu = ", mata_uang)
        elif uang <= 0:
            print("Mohon Masukan nominal uang yang benar dengan angka, bukan huruf!! Jangan memasukan Angka 0")
            continue
        else: ("uang kamu = ", mata_uang)

        #proses pemilihan kategori jenis transaksi
        kategori = input("\nPilih kategori (Penghasilan/Pengeluaran)= ")
        kategori_bersih = kategori.strip().lower()

        if kategori == "penghasilan":
            total_penghasilan = total_penghasilan + uang
            print("Uang kamu = Rp", uang)
            print("Berhasil menambahkan ke Penghasilan\n")
        elif kategori == "pengeluaran":
            total_pengeluaran = total_pengeluaran + uang
            print("Uang kamu = Rp", uang)
            print("Berhasil menambahkan ke Pengeluaran\n")
        else : print("Pilihan kategori tidak valid")

        #variabel nota, agar jumlah uang masuk kedalam riwayat transaksi
        nota_transaksi = {"nominal": uang, "Kategori": kategori_bersih }
        riwayat_transaksi.append(nota_transaksi)
        #buka file mode write 'w', jika file blm ada otomatis ditulis json
        with open(FILE_NAMA, "w") as file_uang:
            #ini akan membuat lembaran tesk baru dari list riwayat transaksi kedalam file json
            #indent=4 agar tulisan file rapi
            json.dump(riwayat_transaksi, file_uang, indent=4)

        print("Nota transaksi sudah disimpan!!")

        
    #menu tampilan 2
    elif pilihan == "2":
        print("--Catatan Riwayat Transaksi--")
        if len(riwayat_transaksi) == 0:
            print("\nBelum ada catatan uang kamu")
        else:
            for index, nota in enumerate(riwayat_transaksi):
                nomor_nota = index + 1
                kategori_bersih = nota["Kategori"]
                uang = nota["nominal"]
                print(f"{nomor_nota}. Kategori : {kategori_bersih}, nominal = {uang}")
        
        print(f"\nTotal Penghasilan : Rp {total_penghasilan:,.0f}".replace(",", "."))
        print(f"Total Pengeluaran : Rp {total_pengeluaran:,.0f}".replace(",", "."))

        dana_bersih = total_penghasilan - total_pengeluaran
        print(f"\nTotal dana bersih kamu = Rp {dana_bersih}")
        print("================================")

    #tampilan 3
    elif pilihan == "3":
        print("\nAplikasi ditutup, Terimakasih")
        break

    else:
        print("Pilihan Tidak Valid!!")
