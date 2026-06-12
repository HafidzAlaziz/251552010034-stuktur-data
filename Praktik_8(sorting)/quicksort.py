def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]
    print(f"Pivot: {pivot}, Less: {less}, Greater: {greater}")
    return quicksort(less) + [pivot] + quicksort(greater)

arr = [10, 90, 80, 30, 70, 60, 20, 50, 40]
sorted_arr = quicksort(arr)
print("Setelah di Sorting:", sorted_arr)