class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data): # ini nambah di depan
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_at_end(head, data): # ini nambah di belakang
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insert_after_node(head, target_data, new_data):
    current = head
    while current and current.data != target_data:
        current = current.next
    
    if current:
        new_node = Node(new_data)
        new_node.next = current.next
        current.next = new_node
        print(f"Berhasil menambahkan {new_data} setelah {target_data}.")
    else:
        print(f"Node dengan data '{target_data}' tidak ditemukan.")
    return head

def print_linked_list(head):
    print("\nIsi Data Saat Ini:")
    temp = head
    while temp:
        print(f"[{temp.data}] --> ", end="")
        temp = temp.next
    print("NULL\n") 

head = None  #inisialisasi awal

# pilihan
while True:
    print_linked_list(head)
    print("Pilih Aksi:")
    print("1. Tambah di Depan")
    print("2. Tambah di Belakang")
    print("3. Tambah setelah Node tertentu")
    print("4. Keluar")
    
    pilihan = input("Masukkan pilihan (1-4): ")
    
    if pilihan == "4":
        break
        
    data_baru = input("Masukkan nama data: ")
    
    if pilihan == "1":
        head = insert_at_beginning(head, data_baru)
    elif pilihan == "2":
        head = insert_at_end(head, data_baru)
    elif pilihan == "3":
        target_data = input("Masukkan nama node target: ")
        head = insert_after_node(head, target_data, data_baru)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    
# head = Node("Ikan")
# head = insert_at_beginning(head, "Cupang") # tambah di depan
# head = insert_at_end(head, "Lele") # tambah di belakang
# insert_after_node(head, "Gurame") # tambah setelah head
# def print_linked_list(head):
#     while head:
#         print(f"[{head.data}] -->", end="")
#         head = head.next
#     print("NULL")

# print_linked_list(head)