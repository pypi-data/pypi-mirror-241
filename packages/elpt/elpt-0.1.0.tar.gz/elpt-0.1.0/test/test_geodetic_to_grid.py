import unittest

from src import geodetic_to_grid

"""Open a terminal and navigate to your project directroy.
Run the test using the following command:
    python -m unittest discover -v test
"""


class TestGeodeticToGrid(unittest.TestCase):
    def test_geodetic_to_grid(self):
        input_var = [
            [(55, 0, 0), (12, 45, 0)],
            [(55, 0, 0), (14, 15, 0)],
            [(57, 0, 0), (12, 45, 0)],
            [(57, 0, 0), (19, 30, 0)],
            [(59, 0, 0), (11, 15, 0)],
            [(59, 0, 0), (19, 30, 0)],
        ]

        result = [
            [6097106.672, 356083.438],
            [6095048.642, 452024.069],
            [6319636.937, 363331.554],
            [6326392.707, 773251.054],
            [6546096.724, 284626.066],
            [6548757.206, 758410.519],
        ]
        xy = []
        for var in input_var:
            phi, lam = var[0], var[1]
            x, y = geodetic_to_grid(phi, lam, ellips="GRS1980", projection="SWEREF99TM")
            x, y = round(x, 3), round(y, 3)
            xy.append([x, y])
        self.assertEqual(result, xy)


if __name__ == "__main__":
    unittest.main()
