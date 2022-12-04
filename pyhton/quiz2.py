#input
nama = str(input("Masukkan nama anda : "))
noHp = int(input("Masukkan nomor handphone anda : "))
menu = str(input("Pilih menu yang diinginkan (Makanan / Minuman) : "))

if menu == "Makanan" :
    print("Nasi Goreng : Rp. 15.000")
    print("Mie Goreng : Rp. 12.000")
    print("Ayam Geprek : Rp. 18.000")

elif menu == "Minuman" :
    print("Aneka Jus : Rp. 15.000")
    print("SoftDrink : Rp. 10.000")
    print("Sweet Ice Tea : Rp. 5.000")

pesanan = str(input("Masukkan pesanan yang diinginkan : "))
jumlahPesanan = int(input("Jumlah pesanan yang diinginkan : "))

print("=============================================================")
#rumus
harga = int

print("Nama anda : ",nama)
print("Nomor handphone anda : ",noHp)

if pesanan == "Nasi Goreng" :
    harga = 15000
    print("Menu yang dipesan : ",pesanan)
    print("Jumlah pesanan : ", jumlahPesanan)
    print("Total harga : Rp.", harga * jumlahPesanan)
elif pesanan == "Mie Goreng" :
    harga = 12000
    print("Menu yang dipesan : ",pesanan)
    print("Jumlah pesanan : ", jumlahPesanan)
    print("Total harga : Rp.", harga * jumlahPesanan)
elif pesanan == "Ayam Geprek" :
    harga = 18000
    print("Menu yang dipesan : ",pesanan)
    print("Jumlah pesanan : ", jumlahPesanan)
    print("Total harga : Rp.", harga * jumlahPesanan)
elif pesanan == "Aneka Jus" :
    harga = 15000
    print("Menu yang dipesan : ",pesanan)
    print("Jumlah pesanan : ", jumlahPesanan)
    print("Total harga : Rp.", harga * jumlahPesanan)
elif pesanan == "SoftDrink" :
    harga = 10000
    print("Menu yang dipesan : ",pesanan)
    print("Jumlah pesanan : ", jumlahPesanan)
    print("Total harga : Rp.", harga * jumlahPesanan)
elif pesanan == "Sweet Ice Tea" :
    harga = 5000
    print("Menu yang dipesan : ",pesanan)
    print("Jumlah pesanan : ", jumlahPesanan)
    print("Total harga : Rp.", harga * jumlahPesanan)