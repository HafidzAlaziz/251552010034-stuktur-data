# panjang k yang memiliki JUMLAH TERBESAR.
angka = [2, 1, 5, 1, 3, 2]
k     = 3
# Tampilkan sub-list dan jumlahnya.

max_jumlah = 0
best_sublist = []

for i in range(len(angka) - k + 1):
    sub_list = angka[i : i + k]
    jumlah = sum(sub_list)
    if jumlah > max_jumlah:
        max_jumlah = jumlah
        best_sublist = sub_list

print("Sub-list terbaik :", best_sublist)
print("Jumlah maksimum  :", max_jumlah)