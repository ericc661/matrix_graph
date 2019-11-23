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


class test_mark_map(unittest.TestCase):

    # 3 plateaus
    def test1(self):
        mg = MatrixGraph([ [4, 5, 2],
                           [1, 5, 5],
                           [2, 3, 1]])
        expected = [[False, True, False],
                    [False, True, True],
                    [False, False, False]]
        self.assertEqual(expected, mg.mark_plateaus())

    # smallest case
    def test2(self):
        mg = MatrixGraph([ [3] ])
        expected = [ [True] ]
        self.assertEqual(expected, mg.mark_plateaus())

    # isolated high points
    def test3(self):
        mg = MatrixGraph([ [1, 8, 2, 5],
                           [6, 7, 4, 3],
                           [9, 8, 2, 3],
                           [1, 4, 2, 2]])
        expected = [[False, True, False, True],
                    [False, False, False, False],
                    [True, False, False, False],
                    [False, False, False, False]]
        self.assertEqual(expected, mg.mark_plateaus())

    # two fail to be a plateau because higher neighbor
    def test4(self):
        mg = MatrixGraph([ [1, 9, 1],
                           [3, 5, 4],
                           [2, 5, 1]])
        expected = [[False, True, False],
                    [False, False, False],
                    [False, False, False]]
        self.assertEqual(expected, mg.mark_plateaus())

    # similar to last except diagonally connected
    # also tests that the region of 1s are not marked plateaus
    def test5(self):
        mg = MatrixGraph([ [4, 5, 2],
                           [5, 1, 5],
                           [8, 1, 1]])
        expected = [[False, False, False],
                    [False, False, False],
                    [True, False, False]]
        self.assertEqual(expected, mg.mark_plateaus())

    # diagonally connected region IS plateaus
    def test6(self):
        mg = MatrixGraph([ [4, 5, 2],
                           [5, 1, 5],
                           [3, 1, 1]])
        expected = [[False, True, False],
                    [True, False, True],
                    [False, False, False]]
        self.assertEqual(expected, mg.mark_plateaus())

    # everything except one high point is a plateau
    def test7(self):
        mg = MatrixGraph([ [5, 5, 5],
                           [5, 5, 5],
                           [5, 5, 9]])
        expected = [[False, False, False],
                    [False, False, False],
                    [False, False, True]]
        self.assertEqual(expected, mg.mark_plateaus())

    # reverse of the last one
    def test8(self):
        mg = MatrixGraph([ [9, 9, 9],
                           [9, 9, 9],
                           [9, 9, 5]])
        expected = [[True, True, True],
                    [True, True, True],
                    [True, True, False]]
        self.assertEqual(expected, mg.mark_plateaus())


    # similar, except diagonally connected
if __name__ == '__main__':
    unittest.main()
