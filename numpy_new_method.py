# !pip install forbiddenfruit -q

from forbiddenfruit import curse
import numpy as np

def numpy_size(self):
    return len(self)

curse(np.ndarray, "size", list_size)

if __name__ == "__main__":
  a = np.array([1, 2, 3])
  print(a.size())
