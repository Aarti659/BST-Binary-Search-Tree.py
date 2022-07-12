class Node:
    def __init__(self, key):
        self.key = key
        self.Left = None
        self.Right = None

def inorder_traverse(root):
    if root is not None:

        inorder_traverse(root.Left)


        print(str(root.key) + "->", end=' ')


        inorder_traverse(root.Right)



def insert(node, key):


    if node is None:
        return Node(key)


    if key < node.key:
        node.Left = insert(node.Left, key)
    else:
        node.Right = insert(node.Right, key)

    return node


def minValueNode(node):
    current = node


    while(current.Left is not None):
        current = current.Left

    return current



def deleteNode(root, key):


    if root is None:
        return root


    if key < root.key:
        root.Left = deleteNode(root.Left, key)
    elif(key > root.key):
        root.Right = deleteNode(root.Right, key)
    else:

        if root.Left is None:
            temp = root.Right
            root = None
            return temp

        elif root.Right is None:
            temp = root.Left
            root = None
            return temp


        temp = minValueNode(root.Right)

        root.key = temp.key


        root.Right = deleteNode(root.Right, temp.key)

    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder_traverse(root)

print("\nDelete 10")
root = deleteNode(root, 10)
print("Inorder traversal: ", end=' ')
inorder_traverse(root)


