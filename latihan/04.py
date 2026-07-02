skor = [45, 90, 12, 75, 80]

def buble_sort(arr):
    n = len(arr)
    jumlah_tukar = 0
    for i in range(n-1):
        for j in range (0, n-i-1):
            if arr[j+1] > arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                jumlah_tukar += 1
        print(f"Iterasi{i+1}: {arr}")
    print(f"Jumlah Tukar: {jumlah_tukar}")
    return arr

hasil = buble_sort(skor)
print(f"Hasil akhir: {hasil}")
