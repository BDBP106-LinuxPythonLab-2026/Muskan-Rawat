import numpy as np

rg=np.random.default_rng(42)
a=rg.random((3,3))
print(a)
print(a[::-1])