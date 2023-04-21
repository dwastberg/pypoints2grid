
# pypoints2grid

Python library wrapping the points2grid algorithm for generate Digital Elevation Models (DEMs)
from pointclouds.




## Acknowledgements

- [Original C++ implementation](https://github.com/CRREL/points2grid/)
- [Information about points2grid algorithm](https://www.opentopography.org/otsoftware/points2grid)

## Usage
Note unlike the original C++ version of points2grid, pypoints2grid doesn't read or write data
from/to file or handle point cloud classification filtering. Use other libraries, like
[laspy](https://laspy.readthedocs.io/en/latest/)
and
[rasterio](https://rasterio.readthedocs.io/en/latest/)
for handeling IO and preparing your data.

```python
from pypoints2grid import points2grid

dem = points2grid(pts, cell_size, bounds=None, radius=0, window_size=3, grid_data = ['idw'], verbose=False)
```

### Parameters
 - __pts__: list of lists or numpy array of shape (n, 3) containing x, y, z coordinates of points
 - __cell_size__: size of the grid cells in meters
 - __bounds__: list of 4 floats containing the bounds of the grid in the form (xmin, ymin, xmax, ymax).
points outside these bounds will be ignored. If None, the bounds will be computed from the points.
 - __radius__: radius of the search circle in meters. If 0, the radius will be computed from the cell size.
 - __window_size__: size of the window used for the moving average filter. If 0, no moving average filter will be applied.
 - __grid_data__: list of strings containing the data interpolations you want returned. Possible values are 
   - 'idw' (inverse distance weighted interpolation)
   - 'min' (minimum of the points in the cell)
   - 'max' (maximum of the points in the cell)
   - 'mean' (mean of the points in the cell)
   - 'std' (standard deviation of the points in the cell)

 - __verbose__: if True, print progress information

### Returns
An (n, m, k) dimensional numpy array containing the interpolated data. n and m are the number of cells in the x and y
directions, and k is the number of data interpolations requested. The order of the data interpolations is the same as 
the order in the __grid_data__ parameter. If k = 1 then the returned array will be 2 dimensional.


## Example

```python
import laspy
import rasterio
from rasterio.transform import Affine
import numpy as np
from time import time

from pypoints2grid import points2grid

las = laspy.read("pointcloud.las")
crs = las.header.parse_crs()

# filter out only ground (classififation 2) and water (classification 9)
ground = las.points[(las.classification == 2) | (las.classification == 9)]
pts = np.vstack((ground.x, ground.y, ground.z)).T

x_min, y_min, z_min = pts.min(axis=0)
x_max, y_max, z_max = pts.max(axis=0)

print(f"loaded {pts.shape[0]} points")
print(f"with bounnds: ({x_min}, {y_min}), ({x_max}, {y_max})")
cell_size = 0.5

print("creating grid")
start_time = time()
dem = points2grid(pts, cell_size)
print(f"grid created in {round(time() - start_time, 2)} seconds")

transform = Affine.transform = Affine.translation(
    x_min - cell_size / 2, y_min - cell_size / 2
) * Affine.scale(cell_size, cell_size)

with rasterio.open(
        "dem.tif",
        "w",
        driver="GTiff",
        height=dem.shape[0],
        width=dem.shape[1],
        count=1,
        dtype=dem.dtype,
        crs=crs,
        transform=transform,
) as dst:
    dst.write(dem, 1)
```


## License

[BSD](https://choosealicense.com/licenses/bsd-4-clause/)

