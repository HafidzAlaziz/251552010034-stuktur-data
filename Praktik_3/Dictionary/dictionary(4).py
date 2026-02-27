users = {
    "kucing": "kcing9999",
    "ayam": "yam0090",
    "ikan": "ikn797"
}

print("From Login")
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

if input_username in users and users[input_username] == input_password:
    print(f"Login {input_username}: Berhasil")
else:
    print(f"Login {input_username}: Gagal")
