# Validasi ekspresi kurung campuran.
# Cek apakah semua tanda kurung ( ), [ ],
# { } berpasangan dan urut dengan benar.

data_tes = ['{[()]}', '{[(])}', '(((']

def cek_valid(teks):
    stack = []
    pasangan = {')': '(', ']': '[', '}': '{'}
    for kurung in teks:
        if kurung in pasangan.values():
            stack.append(kurung)
        elif kurung in pasangan.keys():
            if stack == []:
                return "Tidak valid"
            elif stack.pop() != pasangan[kurung]:
                return "Tidak valid"
    return "Valid" if stack == [] else "Tidak valid"

for data in data_tes:
    print(f"{data} : {cek_valid(data)}")