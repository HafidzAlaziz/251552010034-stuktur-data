# Hitung frekuensi kemunculan setiap kata dari list berikut:
# Tampilkan dictionary hasil hitungan.
# Output yang diharapkan:
# {'apel': 3, 'jeruk': 2, 'mangga': 1}

daftar_kata = ['apel', 'jeruk', 'apel', 'mangga', 'jeruk', 'apel']

jumlah_kata = {}
for i in daftar_kata:
    jumlah_kata.update({i: daftar_kata.count(i)})

print(jumlah_kata)