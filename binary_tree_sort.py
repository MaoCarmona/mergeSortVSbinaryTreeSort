
class TreeNode:
    __slots__ = 'value', 'left', 'right'
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def in_order_traversal(self, node, sorted_list):
        stack, current = [], node
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            sorted_list.append(current.value)
            current = current.right

def binary_tree_sort(arr):
    tree = BinaryTree()
    for value in arr:
        tree.insert(value)
    
    sorted_list = []
    tree.in_order_traversal(tree.root, sorted_list)
    return sorted_list