#program hitung berat badan ideal
#input
tinggiBadan = input("Masukkan tinggi badan anda (dalam centimeter) = ")

#rumus
tinggiBadan2 = (int(tinggiBadan) - 100)* 10/100
beratIdeal = (int(tinggiBadan)-100) - int(tinggiBadan2)

#output
print("Berat badan ideal kamu adalah =", beratIdeal, "Kg")