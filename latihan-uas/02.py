def terbesar(arr):
    terbesar = arr[0]
    terkecil = arr[0]
    for angka in arr[1:]:
        if angka > terbesar:
            terbesar = angka
        if angka < terkecil:
            terkecil = angka
    return terbesar, terkecil

input_list = [4, 1, 9, 3, 7]
terbesar, terkecil = terbesar(input_list)
print(f"Terbesar: {terbesar}")
print(f"Terkecil: {terkecil}")