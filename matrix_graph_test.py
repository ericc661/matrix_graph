import unittest
from matrix_graph import MatrixGraph

class test_get_neighbors(unittest.TestCase):

    # 1x1 matrix
    def test1(self):
        mg = MatrixGraph([[7]])
        neighbors = mg.get_neighbors((0, 0))
        self.assertEqual(len(neighbors), 0)

    # 3x3 matrix, all elements
    def test2(self):
        mg = MatrixGraph([[7, 8, 9], [2, 4, 7], [1, 2, 3]])
        neighbors = mg.get_neighbors((1, 1))
        self.assertEqual(len(neighbors), 8)
        self.assertIn((0, 0), neighbors)
        self.assertIn((0, 1), neighbors)
        self.assertIn((0, 2), neighbors)
        self.assertIn((1, 0), neighbors)
        self.assertIn((1, 2), neighbors)
        self.assertIn((2, 0), neighbors)
        self.assertIn((2, 1), neighbors)
        self.assertIn((2, 2), neighbors)

    # 4x5 matrix, top right corner
    def test3(self):
        mg = MatrixGraph([ [7, 8, 9, 2, 1],
                           [2, 4, 7, 0, 3],
                           [1, 2, 3, 2, 8],
                           [2, 9, 6, 5, 8]])
        neighbors = mg.get_neighbors((0, 4))
        self.assertEqual(len(neighbors), 3)
        self.assertIn((0, 3), neighbors)
        self.assertIn((1, 3), neighbors)
        self.assertIn((1, 4), neighbors)

    # 4x5 matrix, bottom edge
    def test4(self):
        mg = MatrixGraph([ [7, 8, 9, 2, 1],
                           [2, 4, 7, 0, 3],
                           [1, 2, 3, 2, 8],
                           [2, 9, 6, 5, 8]])
        neighbors = mg.get_neighbors((3, 1))
        self.assertEqual(len(neighbors), 5)
        self.assertIn((2, 0), neighbors)
        self.assertIn((2, 1), neighbors)
        self.assertIn((2, 2), neighbors)
        self.assertIn((3, 0), neighbors)
        self.assertIn((3, 2), neighbors)

    # 4x5 matrix, somewhere in the middle
    def test5(self):
        mg = MatrixGraph([ [7, 8, 9, 2, 1],
                           [2, 4, 7, 0, 3],
                           [1, 2, 3, 2, 8],
                           [2, 9, 6, 5, 8]])
        neighbors = mg.get_neighbors((2, 3))
        self.assertEqual(len(neighbors), 8)
        self.assertIn((1, 2), neighbors)
        self.assertIn((1, 3), neighbors)
        self.assertIn((1, 4), neighbors)
        self.assertIn((2, 2), neighbors)
        self.assertIn((3, 4), neighbors)
        self.assertIn((3, 2), neighbors)
        self.assertIn((3, 3), neighbors)
        self.assertIn((3, 4), neighbors)

if __name__ == '__main__':
    unittest.main()
