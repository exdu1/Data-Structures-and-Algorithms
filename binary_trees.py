class Binary_Node:
    def __init__(A, x):
        A.item = x
        A.parent = None
        A.left = None
        A.right = None
    
    def subtree_itr(A):
        if A.left: yield from A.left.subtree_itr() # recursively list left subtree
        yield A # list the node itA
        if A.right: yield from A.right.subtree_itr() # recursively list right subtree

    def subtree_first(A): # no left child
        if A.left: return A.left.subtree_first() 
        else: return A

    def subtree_last(A): # no right child
        if A.right: return A.right.subtree_last()
        else: return A
    
    def successor(A): # next node in traversal order
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent
    
    def predecessor(A):
        if A.left: return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent
    
    def subtree_insert_before(A, new_node):
        if A.left:
            A = A.left.subtree_last()
            A.right = new_node
            new_node.parent = A
        else:
            A.left = new_node
            new_node.parent = A
    
    def subtree_insert_after(A, new_node):
        if A.right:
            A = A.right.subtree_first()
            A.left = new_node
            new_node.parent = A
        else:
            A.right = new_node
            new_node.parent = A

    def subtree_delete(A):
        if A.left or A.right:
            if A.left: B = A.predecessor()
            else: B = A.successor
            A.item = B.item
            B.item = A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A: A.parent.left = None
            else: A.parent.right = None
        return A
    
class Binary_Tree:
    def __init__(T, Node_Type = Binary_Node):
        T.root = None
        T.size = 0
        T.Node_Type = Node_Type

    def len(T): return T.size
    
    def __itr__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield T.item
                

