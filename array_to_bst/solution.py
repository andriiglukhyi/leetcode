class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

def sorted_array_to_bst(arr):
    if not arr:
        return
    mid = len(arr)//2
    root = Node(arr[mid])
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])
    return root

end = []
def preOrder(node):
    # nonlocal end
    if not node:
        return
     
    end.append(node.data)
    preOrder(node.left)
    preOrder(node.right)

arr = [1, 2, 3, 10, 11, 20, 40]
root = sorted_array_to_bst(arr)
preOrder(root)
print(end, arr)