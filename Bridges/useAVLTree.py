from Bridges.Bridges import * 
from Bridges.AVLTreeElement import *
from AVLTree import AVLTree

def useAVLTree(tree_id):

    # create a bridges object
    # Modify the account information
    # !!! Do not modify tree_id. 
    bridges = Bridges(tree_id, "Aritemis", "268629325599")

    #avl = AVLTree('tree'+ str(tree_id) + '.txt')
    avl = AVLTree('c:/Users/My LENOVO/Desktop/other workspace/CMPT306/Bridges/tree'+ str(tree_id) + '.txt')
    
    # add some visual attributes
    avl.get_root().get_visualizer().set_color("magenta")
    avl.get_root().get_visualizer().set_opacity(0.8)

    # set visualizer type
    bridges.set_data_structure(avl.get_root())

    # visualize the tree
    bridges.visualize()

if __name__ == "__main__":

    for tree_id in range(1,5):
        useAVLTree(tree_id)
