import unitttest
from matrix_graph import MatrixGraph

class test_get_neighbors(unittest.TestCase):

    # 1x1 matrix
    def test(self):
        mg = MatrixGraph([[7]])
        neighbors = mg.get_neighbors((0,0))
        self.assertEqual(len(neighbors), 0)

    # 3x3 matrix, all elements
    def test(self):
        mg = MatrixGraph([[7, 8, 9], [2, 4, 7], [1, 2, 3]])
        neighbors = mg.get_neighbors((1,1))
        self.assertEqual(len(neighbors), 8)
        self.assertIn((0, 0), neighbors)
        self.assertIn((0, 1), neighbors)
        self.assertIn((0, 2), neighbors)
        self.assertIn((1, 0), neighbors)
        self.assertIn((1, 2), neighbors)
        self.assertIn((2, 0), neighbors)
        self.assertIn((2, 1), neighbors)
        self.assertIn((2, 2), neighbors)

    # 5x5 matrix, top right corner

    # 5x5 matrix, bottom edge

    # 5x5 matrix, somewhere in the middle

if __name__ == '__main__':
    unittest.main()
