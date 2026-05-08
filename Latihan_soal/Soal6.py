# Balikkan sebuah string menggunakan
# struktur data Stack.
# Input : 'algoritma'
# Lakukan dengan push tiap karakter
# ke stack, lalu pop satu per satu.

def balikin_kata(text):
    kata = []
    for i in text:
        kata.append(i)
    
    hasil = ""
    while kata:
        hasil += kata.pop()

    return hasil

kata = 'algoritma'
print("Kata :",kata)
print("Dibalik :",balikin_kata(kata))
