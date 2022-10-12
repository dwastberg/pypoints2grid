import numpy as np

from _points2grid import _points2grid


def points2grid(pts, cell_size, bounds=None, radius=0, window_size=3, verbose=False):
    if type(pts) is not np.ndarray:
        pts = np.array(pts)
    if len(pts.shape) != 2 or pts.shape[1] != 3:
        raise ValueError(f"points has dimension {pts.shape}. Must have (N,3)")
    check_bounds = True
    if bounds is None:
        x_min, y_min, z_min = pts.min(axis=0)
        x_max, y_max, z_max = pts.max(axis=0)
        check_bounds = False
    else:
        x_min, y_min, x_max, y_max = bounds

    return _points2grid(
        pts,
        cell_size,
        x_min,
        y_min,
        x_max,
        y_max,
        radius,
        window_size,
        check_bounds,
        verbose,
    )
