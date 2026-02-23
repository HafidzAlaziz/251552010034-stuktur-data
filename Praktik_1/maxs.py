angka = [100, 50, 75, 25, 0]

angka.sort()

maks = angka[0]

for a in angka:
    if a > maks:
            maks = a
print(angka)
print("nilai terbesar adalah :" ,maks)