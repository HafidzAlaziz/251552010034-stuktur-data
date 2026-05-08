# Gunakan tuple sebagai key dictionary untuk menyimpan nama mahasiswa berdasarkan koordinat (baris, kolom):
# (1,1)='Andi', (1,2)='Budi', (2,1)='Cici'
# Akses dan tampilkan nama di posisi (1,2).

# CLUE (Kombinasi Catatan 2 dan Catatan 3):
# 1. Ingat di Catatan 2: Tuple menggunakan tanda kurung biasa '()' dan sifatnya "tidak bisa diubah".
#    Oleh karena itu, Tuple sangat cocok dijadikan KEY/kunci di dalam sebuah Dictionary.
# 2. Buat sebuah dictionary (misalnya: posisi_mhs) dan masukkan data di atas.
#    Format penulisan dictionary-nya: 
#    posisi_mhs = {
#       (1, 1): 'Andi',
#       # Lanjutkan untuk Budi dan Cici...
#    }
# 3. Gunakan fungsi .get() dari Catatan 3 untuk "Akses nama di posisi (1,2)"
#    Atau bisa juga langsung memanggil key-nya menggunakan kurung siku: posisi_mhs[(1, 2)]
# 4. Print hasilnya.

# Tulis kodemu di bawah ini:
posisi_mhs = {
    (1, 1): 'Andi',
    (1, 2): 'Budi',
    (2, 1): 'Cici'
}
for koordinat, nama in posisi_mhs.items():
    koordinat_str = f"({koordinat[0]},{koordinat[1]})"
    print(f"Posisi {koordinat_str} : {nama}")

print(f"Di (1,2)     : {posisi_mhs[(1, 2)]}")