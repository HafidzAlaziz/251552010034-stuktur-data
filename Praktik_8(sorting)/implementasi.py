import pandas as pd
import matplotlib.pyplot as plt

data = [
    {"Tanggal": "2025-07-01", "Warna": "Merah", "Ukuran": "M", "Jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-01", "Warna": "Putih", "Ukuran": "L", "Jumlah": 1, "Harga": 30000},
    {"Tanggal": "2025-07-02", "Warna": "Hitam", "Ukuran": "XL", "Jumlah": 3, "Harga": 35000},
    {"Tanggal": "2025-07-03", "Warna": "Merah", "Ukuran": "S", "Jumlah": 4, "Harga": 20000},
    {"Tanggal": "2025-07-03", "Warna": "Putih", "Ukuran": "M", "Jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-04", "Warna": "Hitam", "Ukuran": "L", "Jumlah": 1, "Harga": 30000},
    {"Tanggal": "2025-07-05", "Warna": "Merah", "Ukuran": "XL", "Jumlah": 3, "Harga": 35000},
    {"Tanggal": "2025-07-06", "Warna": "Putih", "Ukuran": "S", "Jumlah": 4, "Harga": 20000},
    {"Tanggal": "2025-07-06", "Warna": "Hitam", "Ukuran": "M", "Jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-07", "Warna": "Merah", "Ukuran": "L", "Jumlah": 1, "Harga": 30000},
    {"Tanggal": "2025-07-08", "Warna": "Hijau", "Ukuran": "XL", "Jumlah": 3, "Harga": 35000},
    {"Tanggal": "2025-07-09", "Warna": "Hijau", "Ukuran": "S", "Jumlah": 4, "Harga": 20000},
    {"Tanggal": "2025-07-10", "Warna": "Hijau", "Ukuran": "M", "Jumlah": 2, "Harga": 25000},
    {"Tanggal": "2025-07-11", "Warna": "Hijau", "Ukuran": "L", "Jumlah": 1, "Harga": 30000},
    {"Tanggal": "2025-07-12", "Warna": "Hijau", "Ukuran": "XL", "Jumlah": 3, "Harga": 35000},
    {"Tanggal": "2025-07-13", "Warna": "Hijau", "Ukuran": "S", "Jumlah": 4, "Harga": 20000},
    {"Tanggal": "2025-07-14", "Warna": "Hijau", "Ukuran": "M", "Jumlah": 2, "Harga": 25000},
]

df = pd.DataFrame(data)
df["Total"] = df["Jumlah"] * df["Harga"]

total_penjualan = df["Total"].sum()

warna_order = ["Merah", "Putih", "Hitam", "Hijau"]
warna_terjual = df.groupby("Warna")["Jumlah"].sum().reindex(warna_order)
total_kaos = warna_terjual.sum()

probabilitas = (warna_terjual / total_kaos) * 100

print("Total Penjualan: Rp {:,.0f}".format(total_penjualan))
print("\nProbabilitas Penjualan per Warna:")
for warna, prob in probabilitas.items():
    print(f"{warna}: {prob:.2f}%")

warna_color_map = {"Merah": "red", "Putih": "white", "Hitam": "black", "Hijau": "green"}
warna_grafik = [warna_color_map[warna] for warna in probabilitas.index]
plt.figure(figsize=(8, 5))
plt.bar(probabilitas.index, probabilitas.values, color=warna_grafik, edgecolor='gray')
plt.title("Probabilitas Pembelian Kaos Berdasarkan Warna")
plt.ylabel("Persentase (%)")
plt.xlabel("Warna Kaos")
plt.ylim(0, 50)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

warna_data = list(zip(warna_terjual.index, warna_terjual.values))

def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][1] < data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

sorted_warna = bubble_sort(warna_data)

print("\nHasil Sorting Warna Berdasarkan Jumlah Terjual:")
for warna, jumlah in sorted_warna:
    print(f"{warna}: {jumlah} kaos")

plt.figure(figsize=(8, 5))
sorted_warna, sorted_jumlah = zip(*sorted_warna)
warna_grafik_sorted = [warna_color_map.get(w, 'gray') for w in sorted_warna]

plt.bar(sorted_warna, sorted_jumlah, color=warna_grafik_sorted, edgecolor='gray')
plt.title("Jumlah Kaos Terjual Berdasarkan Warna (Sorted)")
plt.ylabel("Jumlah Kaos Terjual")
plt.xlabel("Warna Kaos")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()