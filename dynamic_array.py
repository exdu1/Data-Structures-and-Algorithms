from static_array import Array_Seq

class Dynamic_Array_Seq(Array_Seq):
  def __init__(self, r = 2):
    super().__init__()
    self.size = 0
    self.r = r
    self._compute_bounds()
    self._resize(0)

  def __len__(self): return self.size
  def __iter__(self):
    for i in range(len(self)): yield self.A[i]

  def build(self, X):
    for a in X: self.insert_last(a)

  def _compute_bounds(self):
    self.upper = len(self.A)
    self.lower = len(self.A) // (self.r * self.r)