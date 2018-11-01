from Bridges.AVLTreeElement import *

class AVLTree():
    def __init__(self, filename):
        # all nodes
        self.nodes = []

        # read keys from txt file
        File = open(filename)
        for key in File:
            # create an AVL tree elements
            self.nodes.append(AVLTreeElement(int(key)))
            self.nodes[-1].set_label(self.nodes[-1].get_key())
        File.close()

        # initialize the root as empty
        self.root = None

        # build the tree
        self.build()

    # build the tree 
    def build(self):
        # insert node to the tree one by one
        for node in self.nodes:
            self.root = self.insert(node, self.root)

    # insert one node to current tree
    def insert(self, node, root):
        if not root:
            root = node
        # go to the left
        elif node.get_key() < root.get_key():
            root.set_left(self.insert(node, root.get_left()))
        # go to the right
        else:
            root.set_right(self.insert(node, root.get_right()))

        # call self.get_height to set balance factor for the root of current subtree
        # you can use something like:
        #           root.set_balance_factor( calculate the balance factor )
        
        rootBalance = ( self.get_height(root.get_right()) - self.get_height(root.get_left()) )
        root.set_balance_factor(rootBalance)
        
        # balance current subtree if root.get_balance_factor() is greater than 1 or less than -1
        # you can use these library functions:
        #           node.get_key()
        #           node.get_left()
        #           node.set_left()
        #           node.get_right()
        #           node.set_right()
        # for more library functions, please go to http://bridgesuncc.github.io/doc/python-api/current/html/index.html

        nodeBalance = node.get_balance_factor()
        leftBalance = 0
        rightBalance = 0

        if root.get_left() is not None:
            leftBalance = root.get_left().get_balance_factor()

        if root.get_right() is not None:
            rightBalance = root.get_right().get_balance_factor()

        if rootBalance > 1:
            if nodeBalance < leftBalance:
                root = self.right_rotation(root)
            else:
                root.set_left(self.left_rotation(root.get_left()))
                root = self.right_rotation(root)
        elif rootBalance < -1:
            if nodeBalance > rightBalance:
                root = self.left_rotation(root)
            else:
                root.set_right(self.right_rotation(root.get_right()))
                root = self.left_rotation(root)

        return root

    # rotate to the left
    def left_rotation(self, root):
        temp = root
        root = root.get_right()
        oldLeft = root.get_left()
        root.set_left(temp)
        if oldLeft is not None:
            root.get_left().set_right(oldLeft)
        return root

    # rotate to the right
    def right_rotation(self, root):
        temp = root
        root = temp.get_left()
        oldRight = root.get_right()
        root.set_right(temp)
        if oldRight is not None:
            root.get_right().set_left(oldRight)
        return root

    # return the height at current node
    def get_height(self, node):
        if not node:
            return 0
        else:
            return max(self.get_height(node.get_left()), self.get_height(node.get_right()))
        
    # return the root of the tree
    def get_root(self):
        return self.root