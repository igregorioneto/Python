class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node
    
    def search(self, data):
        return self._search(self.root, data)
    
    def _search(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search(node.left, data)
        return self._search(node.right, data)
    
    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node.data, end=" ")
            self._in_order(node.right)

if __name__ == "__main__":
    bst = BinarySearchTree()
    elementos = [8, 3, 10, 1, 6, 4, 7, 14, 13]
    for elem in elementos:
        bst.insert(elem)

    print("BST In-Order:")
    bst.in_order()

    print("\nBusca pelo valor 7:")
    resultado = bst.search(7)
    if resultado:
        print("Encontrado:", resultado.data)
    else:
        print("Não encontrado")