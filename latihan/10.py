def quick_sort(arr, low, high, comps):
    if low < high:
        pi = partition(arr, low, high, comps)
        quick_sort(arr, low, pi - 1, comps)
        quick_sort(arr, pi + 1, high, comps)

def partition(arr, low, high, comps):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comps[0] += 1
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [10, 7, 8, 9, 1, 5]
comps = [0]
print(f"List asli: {arr}")
quick_sort(arr, 0, len(arr) - 1, comps)
print(f"Hasil sort: {arr}")
print(f"Total perbandingan: {comps[0]}")