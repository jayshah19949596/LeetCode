class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        no_of_rows = len(matrix)
        no_of_cols = len(matrix[0])
        self.transpose(matrix, no_of_rows, no_of_cols)
        self.reverse_rows(matrix, no_of_rows, no_of_cols)
        
    def transpose(self, matrix, no_of_rows, no_of_cols):
        
        for i in range(no_of_rows):
            for j in range(i, no_of_cols):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                
    def reverse_rows(self, matrix, no_of_rows, no_of_cols):
        for i in range (no_of_rows):
             for j in range(no_of_cols//2):
                matrix[i][j], matrix[i][no_of_cols-1-j] = matrix[i][no_of_cols-1-j], matrix[i][j]
                

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1  # last index
        layers = len(matrix) // 2  # number of rings
        for layer in range(layers):
            last = n - layer
            # iterate all column elements in top row of the layer
            for i in range(layer, last):
                # clockwise swap
                temp = matrix[layer][i]                      # save top 
                matrix[layer][i] = matrix[n - i][layer]      # lft col → top row
                matrix[n - i][layer] = matrix[last][n - i]   # dwn row → lft col
                matrix[last][n - i] = matrix[i][last]        # ryt col → dwn row
                matrix[i][last] = temp                       # top row → ryt col
