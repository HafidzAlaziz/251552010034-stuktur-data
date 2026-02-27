user = {"name": "Ayam", "age": 2, "color": "Putih"}

email = user.get("email", "Email tidak tersedia")
print("Email:", email)

user.setdefault("email", "ayam@example.com")

user.update({"age": 3, "color": "Hitam"})

age = user.pop("age")

print(user.keys())
print(user.values())

user_copy = user.copy()
print("Salinan user:", user_copy)

print(user_copy)