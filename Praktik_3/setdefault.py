# Alamat = {'A':'Bogor'}

# print("Sebelum di setdefault:" ,Alamat)

# alamat_baru = Alamat.setdefault('B', 'Bandung')

# print("Alamat baru yang ditambahkan:", Alamat)

kontak = {'Fadhli': '08123456789'}
print("Sebelum setdefault:", kontak)
kontak.setdefault('Andi', '08234567890')
kontak.setdefault('Fadhli', '09000000000')
print("Setelah setdefault:", kontak)