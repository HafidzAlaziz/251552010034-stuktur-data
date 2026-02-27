Gudang = {
    "palu" : 10,
    "obeng" : 15,
    "kunci inggris" : 5,
}
print("------------Jumlah alat sebelum di update------------")
print("palu:", Gudang["palu"])
print("obeng:", Gudang["obeng"])
print("kunci inggris:", Gudang["kunci inggris"])

print("-----------Update jumlah alat:-----------------")
Gudang["palu"] = 12
print("Jumlah palu setelah di update:", Gudang["palu"])

Gudang["obeng"] -= 3
print("Jumlah obeng setelah di update:", Gudang["obeng"])

print("------------Jumlah alat setelah di update------------")
print("palu:", Gudang["palu"])
print("obeng:", Gudang["obeng"])
print("kunci inggris:", Gudang["kunci inggris"])