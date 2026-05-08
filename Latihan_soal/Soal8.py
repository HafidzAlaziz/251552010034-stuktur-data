# Two-Pointer: Cari semua pasangan
# bilangan dalam list terurut yang
# jumlahnya sama dengan target.
# Gunakan dua pointer (kiri & kanan).
angka  = [1, 2, 3, 4, 6, 8, 9]
target = 10
kiri = 0
kanan = len(angka) - 1

while kiri < kanan:
    jumlah = angka[kiri] + angka[kanan]
    if jumlah == target:
        print(f"({angka[kiri]}, {angka[kanan]})")
        kiri += 1
        kanan -= 1
    elif jumlah < target:
        kiri += 1
    else:
        kanan -= 1
