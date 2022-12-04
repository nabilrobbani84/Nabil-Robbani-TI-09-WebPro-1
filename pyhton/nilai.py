#input
nama = input("Masukkan nama anda : ")
umur = input("Masukkan umur anda : ")
kelas = input("Masukkan kelas anda : ")

#rumus
if int(nilai) > 89 :
    ket = "istimewa"
if int(nilai) > 69 :
    ket = "sangat bagus"    
if int(nilai) > 59 :
    ket = "cukup"    
else :
    ket = "gagal"

#output
print("Nama anda : ", nama)
print("kelas anda : ", kelas)
print("Nilai anda : ", nilai)
print(ket)