def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
        
    print(f"Counting array: {count}")
    
    hasil = []
    for i in range(len(count)):
        hasil.extend([i] * count[i])
    return hasil

arr = [4, 2, 2, 8, 3, 3, 1]
print(f"Array asli: {arr}")
hasil = counting_sort(arr)
print(f"Hasil sort: {hasil}")