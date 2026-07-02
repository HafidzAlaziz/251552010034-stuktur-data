# Konversi bilangan desimal ke biner
# menggunakan Stack.
# Desimal: 42
# Algoritma: bagi 2 terus, sisa bagi
# (0 atau 1) di-push ke stack, lalu
# pop untuk membentuk biner.

def desimal_ke_biner(desimal):
    stack = []
    while desimal > 0:
        sisa = desimal % 2
        stack.append(sisa)
        desimal = desimal // 2
    biner = ""
    while stack:
        biner += str(stack.pop())
    return biner
    
desimal = 42
print("Desimal :", desimal)
print("Biner   :", desimal_ke_biner(desimal))