# Dua kelas mengikuti dua ekskul berbeda:
basket  = {'Andi','Budi','Cici','Deni'}
futsal  = {'Budi','Deni','Eko','Fani'}
# Tampilkan: siapa ikut KEDUANYA, siapa
# ikut SALAH SATU saja (bukan keduanya).

print("Mengikuti 2 duanya : ", basket.intersection(futsal))
print("Mengikuti salah satu : ", basket.symmetric_difference(futsal))
