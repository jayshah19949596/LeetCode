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
                
class Solution1:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        layers = len(matrix)//2
        n = len(matrix)-1
        for layer in range(layers):
            for i in range(layer, n - layer):
                temp = matrix[layer][i]
                matrix[layer][i] = matrix[n - i][layer]
                matrix[n - i][layer] = matrix[n - layer][n - i]
                matrix[n - layer][n - i] = matrix[i][n - layer]
                matrix[i][n - layer] = temp
            
