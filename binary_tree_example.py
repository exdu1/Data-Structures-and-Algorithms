class Binary_Node:
  def __init__(self, x): # O(1)
    self.item = x
    self.left = None
    self.right = None
    self.parent = None
    #node.subtree_update()
  
  # find the traversal order recursively
  def subtree_itr(self): # O(n)
    if self.left: yield from self.subtree_itr() 
    if self.right: yield from self.subtree_itr()    
  
  # left most node
  def subtree_first(self):
    if self.left: return self.left.subtree_first()
    else: return self
  
  # right most node
  def subtree_last(self):
    if self.right: return self.right.subtree_last()
    else: return self
  
  # next node in traversal order
  def successor(self): 
    if self.right: return self.right.subtree_first()
    while self.parent and (self is self.parent.right):
      self = self.parent
    return self.parent
     
  # previous node in traversal order
  def predecessor(self):
    if self.left: return self.left.subtree_last()
    while self.parent and (self is self.parent.right):
      self = self.parent
    return self.parent
  
  def subtree_insert_before(self, new_node):
    # if no left, insert left
    # otherwise shift some pointers
    if self.left:
      self = self.left.subtree_last()
      self.right = new_node
      new_node.parent = self
    else:
      self.left = new_node
      new_node.parent = self
    # self.maintain()                      # wait for R07!

  def subtree_insert_after(self, new_node):
    # if no right, insert right
    # shift some pointers
    if self.right:
      self = self.right.subtree_last()
      self.right = new_node
      new_node.parent = self
    else:
      self.right = new_node
      new_node.parent = self
      # self.maintain()                      # wait for R07!

  def subtree_delete(self):
    # if leaf, detach from the parent
    # keep swapping self down the tree until self is leaf
    if self.left or self.right: 
      if self.right: new_node = self.predecessor()
      else: new_node = self.successor()
    