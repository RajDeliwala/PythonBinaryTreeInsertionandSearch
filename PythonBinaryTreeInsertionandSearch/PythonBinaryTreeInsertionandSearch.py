'''
Cracking the coding interview
Chapter 4 - Binary Trees
Page 100
----------------------------------------
Summary: Learning Binary Trees in Python - Search and Insertion
Constraits or Questions you need to ask:
Solution notes:
'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    #Helper function to print each order
    def printTree(self, traversalType):
        if traversalType == "preorder":
            return self.preOrderPrint(tree.root, "")
        elif traversalType == "inorder":
            return self.inOrderPrint(tree.root, "")
        elif traversalType == "postorder":
            return self.postOrderPrint(tree.root, "")
        else:
            print("Travesal type " + str(traversalType) + " is not supported")
            return False

    #Recursive solution to print in preorder
    def preOrderPrint(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preOrderPrint(start.left, traversal)
            traversal = self.preOrderPrint(start.right, traversal)
        return traversal

    #Recursive solution to print in inorder
    def inOrderPrint(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inOrderPrint(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inOrderPrint(start.right, traversal)
        return traversal

    #Recursive solution to print in postorder
    def postOrderPrint(self, start, traversal):
        """Left -> Right -> Root"""
        if start:
            traversal = self.postOrderPrint(start.left, traversal)
            traversal = self.postOrderPrint(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def insert(self,data):
        if self.root is None:
            Node(data)
        else:
            self._insert(data, self.root)


    def _insert(self, data, cur_node):
        if data < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else: 
                self._insert(data, cur_node.right)
        else:
            print("The value is already present in the tree. ")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):
        if data > cur_node.value and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.value and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.value:
            return True




BST = BinaryTree(1)
BST.insert(4)
BST.insert(2)
BST.insert(8)
BST.insert(5)
BST.insert(10)

print(BST.find(5)) #Retruns True
print(BST.find(21)) #Returns False




