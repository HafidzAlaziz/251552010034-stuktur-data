from collections import deque
queue = deque(['Andi', 'Budi', 'Citra', 'Doni', 'Eka'])
print(f"Antrian saat ini : {queue}\n")

for i in range (3):
    orang = queue.popleft()
    print(f"{orang} dipanggil dan keluar dari antrean")

print(f"\nAntrian tersisa: {queue}")