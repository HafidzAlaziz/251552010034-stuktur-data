user = {
    "Hewan": "Kucing",
    "Warna": "Hitam",
    "Umur": "3 Tahun"
}
print("---------Sebelum diubah:---------")
print("Hewan:", user["Hewan"])
print("Warna:", user["Warna"])
print("Umur:", user["Umur"])

user["email"] = "kcing8089@gmail.com"
user["warna"] = "Putih"
user["umur"] = "4 Tahun"

print("---------Setelah diubah:---------")
print("Hewan:", user["Hewan"])
print("Warna:", user["Warna"])
print("Umur:", user["Umur"])
print("Email:", user["email"])