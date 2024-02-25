class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def findMaxValue(node):
    current = node
    # Йдемо до найправішого вузла, який не має правого нащадка
    while current.right:
        current = current.right
    return current.key

# Створимо BST для прикладу
root = None
keys = [15, 10, 20, 8, 12, 17, 25]
for key in keys:
    root = insert(root, key)

# Знайдемо найбільше значення
max_value = findMaxValue(root)
print("Найбільше значення в дереві:", max_value)