kendaraan = ["mobil","mobil", "mobil", "motor", "sepeda", "bus", "truk", "motor"]
hasil = []

for item in kendaraan:
    if item not in hasil:
        hasil.append(item)

print("tanpa duplikat:", hasil)