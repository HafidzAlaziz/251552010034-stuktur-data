nilai_mahasiswa = [55, 75, 80, 40, 90, 65]
nilai_lulus = []  # Tempat untuk menyimpan nilai yang 70 ke atas

for i in nilai_mahasiswa:
    if i >= 70:
        nilai_lulus.append(i)


print(f"Daftar nilai yang lulus: {nilai_lulus}")