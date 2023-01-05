import numpy as np

from _points2grid import _points2grid
from enum import Enum

class GridData(Enum):
    IDW = 1 << 0
    MIN = 1 << 1
    MAX = 1 << 2
    MEAN = 1 << 3
    STD = 1 << 4

def points2grid(pts, cell_size, bounds=None, radius=0, window_size=3, grid_data = ['idw'], verbose=False):
    if type(pts) is not np.ndarray:
        pts = np.array(pts)
    if len(pts.shape) != 2 or pts.shape[1] != 3:
        raise ValueError(f"points has dimension {pts.shape}. Must be (N,3)")
    
    check_bounds = True
    if bounds is None:
        x_min, y_min, z_min = pts.min(axis=0)
        x_max, y_max, z_max = pts.max(axis=0)
        check_bounds = False
    else:
        x_min, y_min, x_max, y_max = bounds

    if len(grid_data) == 0:
        grid_data = ['idw']
    grid_data = [GridData[x.upper()].value for x in grid_data]
    grid_data_enum = sum(grid_data)
    

    result =  _points2grid(
        pts,
        cell_size,
        x_min,
        y_min,
        x_max,
        y_max,
        radius,
        window_size,
        check_bounds,
        grid_data_enum,
        verbose,
    )
    result = np.squeeze(result)
    if len(grid_data) > 1:
        grid_data_args = np.argsort(grid_data)
        result = result[:, :, grid_data_args]
        pass
    return result