# Tanpa menggunakan fungsi min() atau max(),
# cari nilai terbesar dan terkecil dari:
# angka = [34, 7, 23, 32, 5, 62]
# Gunakan perulangan dan percabangan.

angka = [34, 7, 23, 32, 5, 62]

terbesar = angka[0]
terkecil = angka[0]

for i in angka:
    if i > terbesar:
        terbesar = i
    if i < terkecil:
        terkecil = i
        
print("Angka :", angka)
print("Nilai terbesar: ", terbesar)
print("Nilai terkecil: ", terkecil) 
