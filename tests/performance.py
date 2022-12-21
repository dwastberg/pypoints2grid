from pypoints2grid import points2grid

import numpy as np

import time

pts = np.random.rand(5000000, 3)
pts[:,:2] *= 100

start = time.time()
dem = points2grid(pts, 0.1)
end = time.time()
print(f"points2grid took {end-start} seconds")
print(dem.shape)