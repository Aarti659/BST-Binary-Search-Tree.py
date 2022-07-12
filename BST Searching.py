class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



def Insert(root, key):

    if root is None:
        return Node(key)


    if key < root.data:
        root.left = Insert(root.left, key)


    else:
        root.right = Insert(root.right, key)

    return root



def search(root, key, parent):

    if root is None:
        print('Key not found')
        return

    if root.data == key:

        if parent is None:
            print(f'The node with key {key} is root node')
        elif key < parent.data:
            print('The given key is the left node of the node with key', parent.data)
        else:
            print('The given key is the right node of the node with key', parent.data)

        return



    if key < root.data:
        search(root.left, key, root)
    else:
        search(root.right, key, root)


if __name__ == '__main__':

    keys = [25, 10, 14, 8, 22, 16,65]

    root = None
    for key in keys:
        root = Insert(root, key)

    search(root, 22, None)






