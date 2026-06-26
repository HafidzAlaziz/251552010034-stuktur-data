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
    if root:
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)

def postorder(root, result):
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.value)

# Membuat tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

res_pre = []; preorder(root, res_pre)
res_in = []; inorder(root, res_in)
res_post = []; postorder(root, res_post)

print(f"Preorder: {res_pre}")
print(f"Inorder: {res_in}")
print(f"Postorder: {res_post}")