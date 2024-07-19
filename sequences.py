# Array sequence
class Array_Seq:
    def __init__(self):
        self.A = []
        self.size = 0

    def __len__(self): return self.size
    def __iter__(self): yield from self.A
    
    def build(self, X):
        self.A = [a for a in X]
        self.size = len(self.A)

    def get_at(self, i): return self.A[i]
    def set_at(self, i, x): self.A[i] = x

    def _copy_forward(self, i, n, A, j):
        for k in range(n):
            A[j + k] = self.A[i + k]

    def _copy_backward(self, i, n, A, j):
        for k in range(n - 1, -1, -1): #start = last index, stop = first index, step = -1 (decrement by 1)
            A[j + k] = self.A[i + k]

    def insert_at(self, i, x):
        n = len(self)
        A = [None] * (n + 1) #initialize new array of size n+1 with 'None'
        self._copy_forward(0, i, A, 0) #copy from start to i
        A[i] = x #insert value at i
        self._copy_forward(i, n - i, A, i + 1) #copy remaining elements
        self.build(A)

    def delete_at(self, i):
        n = len(self)
        A = [None] * (n - 1)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i + 1, n - i - 1, A, i) # n - i - 1 copy the remaining elements minus 1 (deleted element)
        self.build(A)
        return x

    def insert_first(self, x): self._insert_at(0, x)

    def delete_first(self): return self._delete_at(0)

    def insert_last(self, x): self._insert_at(len(self), x)

    def delete_last(self): return self._delete_at(len(self) - 1)

    def show(self):
        for x in self:
            print(x, end=' ')

array_seq = Array_Seq()
array_seq.build([0, 1, 2, 3, 4, 5, 6, 7, 8])

print('Before delete at')
array_seq.show()

array_seq.delete_at(0)
print('After delete at')
array_seq.show()


