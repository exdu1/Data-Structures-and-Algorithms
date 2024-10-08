class Linked_List_Node():
  def __init__(self, x):
    self.item = x                              # data
    self.next = None                           # pointer
  
  def later_node(self, i):                     # recursively find node at position i
    if i == 0: return self                     # i = positions ahead of current node
    assert self.next                           # ensure next node exists (throws AssertationError otherwise)
    return self.next.later_node(i - 1)         # recurssion


class Linked_List_Seq:
  def __init__(self):
    self.head = None                           # pointer to the beginning of the list
    self.size = 0
  
  def __len__(self): return self.size

  def __iter__(self):
    node = self.head
    while node:
      yield node.item
      node = node.next

  def build (self, X):
    for a in reversed(X):
      self.insert_first(a)

  def get_at(self, i):
    node = self.head.later_node(i)            # find the ith node from the head
    return node.item
  
  def set_at(self, i, x):
    node = self.head.later_node(i)            # iterate through the list and find the ith node
    node.item = x                             # set the ith node's value
  
  def insert_first(self, x):
    new_node = Linked_List_Node(x)
    new_node.next = self.head
    self.head = new_node
    self.size += 1

  def delete_first(self):
    x = self.head.item
    self.head = self.head.next
    self.size -= 1
    return x 
  
  def insert_at(self, i, x):
    if i == 0:
      self.insert_first(x)
      return
    new_node = Linked_List_Node(x)
    node = self.head.later_node(i - 1)     # placeholder for the node pointer to the ith node
    new_node.next = node.next              
    node.next = new_node
    self.size += 1

  def delete_at(self, i):
    if i == 0:
      return self.delete_first()
    node = self.head.later_node(i - 1)
    x = node.next.item
    node.next = node.next.next
    self.size -= 1
    return x
  
  def insert_last(self, x): self.insert_at(len(self), x)
  def delete_last(self): return self.delete_at(len(self) - 1)


