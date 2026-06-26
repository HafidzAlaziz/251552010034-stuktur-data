def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Iterasi {i + 1}: {arr}")
    return arr

input_arr = [64, 34, 25, 12, 22]
hasil = bubble_sort(input_arr)
print(f"Hasil akhir: {hasil}")