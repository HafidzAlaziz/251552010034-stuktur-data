def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Step {i + 1}: {arr}")

arr = [10, 23, 4, 9, 90, 70, 99, 1]
selection_sort(arr)
print("Setelah di Sorting:", arr)