'''
This class takes in a 2D matrix of numbers, required to be at least 1x1.
It contains a variety of functions that find properties of the graph.
'''

class MatrixGraph:
    '''
    summary: initializes and stores matrix as member variable
    requires: matrix to be a List[List[int]] where len(matrix) > 0
      and len(matrix[0]) > 0
    effects: see above
    '''
    def __init__(self, matrix):
        self.matrix = matrix

    '''
    summary: returns a matrix of same dimensions as input indicating plateau
      high points - marks the entire map as opposed to starting at one coordinate
    requires: nothing
    effects: returns a List[List[bool]], true for every coordinate that is a
      plateau high point (see below for definition).
    '''
    def mark_plateaus(self):
        # init matrix of bools same size as input matrix
        self.plateau_matrix = [[None] * len(self.matrix[0])] * len(self.matrix)
        raise NotImplementedError()

    '''
    summary: given a start coordinate, determines if it is a plateau high point
      and marks it and its connected plateau high points (if applicable)
      accordingly
    requires: start vertex to be in bounds of the matrix
    effects: Marks the coordinate True if it is a plateau high point.
      A coordinate may be a plateau high point if the matrix's value at that
      coordinate is greater than or equal to all its neighbors, 8-directionally.
      However, for all neighbors that have equal height (if any), those
      neighbors must in turn be a plateau high point. If a coordinate is a
      plateau high point, this function returns true and marks it and all connected
      plateau high points true in the return matrix. Otherwise, leaves the
      coordinate's value default (False)
    '''
    def mark_pleateau_region(self, start):
        raise NotImplementedError()

    '''
    summary: given a coordinate, returns the coordinates of the neighbors of a
      cell given they are in range (not outside the dimensions of the matrix)
    requires: coord to a be tuple (row, column) that represents the location of
      a cell in bounds
    effects: returns a list of all the neighbors of coord in bounds
    '''
    def get_neighbors(self, coord):
        (row, col) = coord
        neighborlist = [(-1, -1), (-1, 0), (-1, 1),
                        (0, -1), (0, 1),
                        (1, -1), (1, 0), (1, 1),]

        neighbors = [(row+x, col+y) for (x, y) in neighborlist
                      if 0 <= row+x < len(self.matrix) and \
                         0 <= col+y < len(self.matrix[0]) ]

        return neighbors

def main():
    pass

if __name__ == '__main__':
    main()
