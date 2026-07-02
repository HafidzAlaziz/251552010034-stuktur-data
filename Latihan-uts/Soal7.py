# Simulasikan antrian printer.
# Job masuk: 'Laporan','Foto','Tugas'
# Printer memproses (dequeue) satu per satu 
# sambil menampilkan job yang sedang dicetak dan sisa antrian.

antrian = ['Laporan', 'Foto', 'Tugas']

print("Antrian :", antrian)
while antrian:
    job = antrian.pop(0)
    print("Cetak   :", job, "| Sisa:", antrian)
