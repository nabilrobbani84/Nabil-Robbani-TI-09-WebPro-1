#input
nama = input("Masukkan nama anda : ")
umur = input("Masukkan umur anda : ")
tinggi = input("Masukkan tinggi anda : ")

#logika
if int(tinggi) >= 90 :
    ket = "Anda boleh bermain"
else :
    ket = "Anda tidak boleh bermain"

#output
print("Nama anda : ", nama)
print("Umur anda : ", umur)
print("Tinggi anda : ", tinggi)
print(ket)