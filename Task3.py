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

def sumOfValues(node):
    if node is None:
        return 0
    else:
        return node.key + sumOfValues(node.left) + sumOfValues(node.right)

# Створимо BST для прикладу
root = None
keys = [15, 10, 20, 8, 12, 17, 25]
for key in keys:
    root = insert(root, key)

# Обчислимо суму всіх значень у дереві
total_sum = sumOfValues(root)
print("Сума всіх значень у дереві:", total_sum)