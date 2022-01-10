# !pip install forbiddenfruit -q

from forbiddenfruit import curse
import numpy as np

def numpy_size(lst):
    return np.prod(lst.shape)

curse(np.ndarray, "size", numpy_size)

if __name__ == "__main__":
    a = np.array([1, 2, 3])
    print(a.size())
