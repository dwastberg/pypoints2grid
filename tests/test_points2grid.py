import unittest

from pypoints2grid import points2grid

import numpy as np


class TestDemSize(unittest.TestCase):
    def setUp(self) -> None:
        self.pts = np.random.rand(1000, 3)

    def test_dem_size(self):
        dem = points2grid(self.pts, 0.1)
        self.assertEqual(dem.shape, (10, 10), "incorrect dem size")

        dem2 = points2grid(self.pts, 0.01)
        self.assertEqual(dem2.shape, (100, 100), "incorrect dem size")

    def test_dem_bounding_box(self):
        bounds = (0.25, 0.25, 0.75, 0.75)
        dem = points2grid(self.pts, 0.01, bounds=bounds)
        self.assertEqual(dem.shape, (50, 50), "incorrect bounded dem size")

class TestDemValues(unittest.TestCase):
    def setUp(self) -> None:
        pt_count = 10000
        xy = np.random.rand(pt_count, 2)
        z = np.ones(pt_count).reshape((-1,1))
        self.pts = np.hstack((xy,z))
        
    def test_dem_values(self):
        dem = points2grid(self.pts, 0.01)
        self.assertTrue(np.alltrue(dem==1))


if __name__ == "__main__":
    unittest.main()
