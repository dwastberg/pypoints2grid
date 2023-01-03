from pypoints2grid import points2grid
from statistics import mean, stdev
import numpy as np

import time

np.random.seed(0)
pts = np.random.rand(5000000, 3)
pts[:,:2] *= 100


times = []
for i in range(3):
    start = time.time()
    dem = points2grid(pts, 0.1)
    times.append(time.time() - start)

print(f"points2grid took {mean(times)} seconds with a standard deviation of {stdev(times)}")
print(dem.shape)