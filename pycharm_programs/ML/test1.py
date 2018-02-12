from scipy import linalg, optimize
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

a = np.array([1, 4, 5, 8], float)
print a
print type(a)

a = np.array([[6, 4], [5, 9]], float)
sel = (a >= 6)
print a[sel]