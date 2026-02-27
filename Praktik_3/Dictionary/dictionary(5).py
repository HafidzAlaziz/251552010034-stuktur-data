users = {
    "kucing": "kcing9999",
    "ayam": "yam0090",
    "ikan": "ikn797"
}

login_attempts =[
    ("kucing", "kcing9999"),
    ("ayam", "yam0090"),
    ("ikan", "ikn797"),
    ("kucing", "wrongpassword"),
    ("sapi", "password")
]

for username, password in login_attempts:
    if username in users and users[username] == password:
        print(f"Login {username}: Berhasil")
    else:
        print(f"Login {username}: Gagal")