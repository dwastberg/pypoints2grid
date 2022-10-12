from tabnanny import verbose
from pypoints2grid import points2grid

import numpy as np

print("Hello world")

pts = np.random.rand(100,3)

dem = points2grid(pts,0.1, window_size = 7, verbose = True)
print(dem.shape)