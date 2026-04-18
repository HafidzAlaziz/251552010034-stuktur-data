def cek_tanda(ekspresi):
    stack = []
# Mapping kurung tutup → kurung buka pasangannya
    pasangan = {')': '(', ']': '[', '}': '{'}

    for char in ekspresi:
        if char in '([{':                                    # kurung buka → push
            stack.append(char)

        elif char in ')]}':                                  # kurung tutup
            if not stack:
                return False                                 # tutup tanpa buka = false
            if stack[-1] != pasangan[char]:
                return False                                 # pasangan tidak cocok
            stack.pop()                                      # cocok → pop kurung bukanya
    return len(stack) == 0                                   # valid jika stack kosong di akhir

# Uji coba cek tanda kurung kurang atau pas
print(cek_tanda('(())')) 
print(cek_tanda('{[()]}')) 
print(cek_tanda('([)]')) 
print(cek_tanda('{[}')) 