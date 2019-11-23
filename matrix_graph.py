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
      high points - marks the entire map
    requires: nothing
    effects: returns a List[List[bool]], true for every coordinate that is a
      plateau high point (see below for definition).
    '''
    def mark_plateaus(self):
        # init matrix of bools same size as input matrix
        self.plateau_matrix = []
        for i in range(len(self.matrix)):
            self.plateau_matrix.append([None] * len(self.matrix[0]))

        for i in range(len(self.plateau_matrix)):
            for j in range(len(self.plateau_matrix[0])):
                # if we haven't marked this coordinate yet
                if self.plateau_matrix[i][j] is None:
                    self.mark_plateau_region((i, j))

        return self.plateau_matrix

    '''
    summary: marks a region of connected same-height coordinates as true if they
      are ALL plateau high points, false if they are all not
    requires: start vertex to be in bounds of the matrix
    effects: See summary.
      A coordinate may be a plateau high point if the matrix's value at that
      coordinate is greater than or equal to all its neighbors, 8-directionally.
      However, for all neighbors that have equal height (if any), those
      neighbors must in turn be a plateau high point. If a same-height region is a
      plateau, this function returns true and marks the enitre region true in the return matrix.
      Otherwise, marks them false.
    '''
    def mark_plateau_region(self, start):
        q = [] # queue for BFS traversal of equal-height coords
        region = [] # stores all equal-height connected coordinates, serves as visited state
        q.append(start)
        region.append(start)
        higher_point_found = False # flag set true if ANY coords see higher point

        while q:
            (row, col) = q.pop(0) # row and column of current coord
            neighbors = self.get_neighbors((row, col))
            for (i, j) in neighbors:
                if self.matrix[i][j] > self.matrix[row][col]:
                    higher_point_found = True #'ruins' region being plateau high points
                elif self.matrix[i][j] == self.matrix[row][col]:
                    if (i, j) not in region: # if not yet visited
                        q.append((i, j))
                        region.append((i, j))

        # at this point, we have entire connected region and whether
        #   region is plateau high points or not
        is_plateau = not higher_point_found
        for (i, j) in region:
            self.plateau_matrix[i][j] = is_plateau

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
