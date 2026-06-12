def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Step {i}: {arr}")

arr = [100, 200, 50, 25, 75, 150, 125, 175]
insertion_sort(arr)
print("Setelah di Sorting:", arr)