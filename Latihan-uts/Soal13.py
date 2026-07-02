# 13. Kelompokkan mahasiswa berdasarkan grade:
#   A: nilai >= 85
#   B: nilai >= 70
#   C: nilai < 70

data = {'Andi':88,'Budi':72,'Cici':65, 'Deni':91,'Eka':68,'Fani':76}

def kelompokkan_mahasiswa(data):
    grade = {'A': [], 'B': [], 'C': []}
    for nama, nilai in data.items():
        if nilai >= 85:
            grade['A'].append(nama)
        elif nilai >= 70:
            grade['B'].append(nama)
        else:
            grade['C'].append(nama)
    return grade

hasil = kelompokkan_mahasiswa(data)
for kelompok, daftar_nama in hasil.items():
    print(f"{kelompok}: {daftar_nama}")
