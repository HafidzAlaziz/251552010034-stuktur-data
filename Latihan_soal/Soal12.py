# 12. Hot Potato Problem: N orang berdiri melingkar, 
# lempar kentang sebanyak k kali.
# Orang yang pegang kentang saat hitungan habis -> keluar. 
# Siapa yang tersisa?

orang = ['Ali','Budi','Cici','Deni','Eka']
k = 3

def hot_potato(orang, k):
    while len(orang) > 1:
        for i in range(k - 1):
            orang.append(orang.pop(0))
        yang_keluar = orang.pop(0)
        print(f"Keluar: {yang_keluar}")
    print(f"Pemenang: {orang[0]}")

hot_potato(orang, k)