class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root, result):
    if root:
        result.append(root.value)
        preorder(root.left, result)
        preorder(root.right, result)
def inorder(root, result):
    if root :
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)
def postorder(root, result):
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.value)

def jumlahkan_tree(root):
    if not root:
        return 0
    node_saat_ini = root.value
    total_kiri = jumlahkan_tree(root.left)
    total_kanan = jumlahkan_tree(root.right)
    return node_saat_ini + total_kiri + total_kanan

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

hasil = jumlahkan_tree(root)
print(f"Jumlah angka dalam tree : {hasil}")

