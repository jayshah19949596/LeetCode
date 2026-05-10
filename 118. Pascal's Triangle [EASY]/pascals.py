class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return [] # Handle edge case
        
        res = [[1]]
        for row in range(1, numRows):
            no_of_ele = row + 1
            cur_row = [1]
            # Use the previous row in res to calculate middle elements
            for j in range(no_of_ele - 2):
                cur_row.append(res[-1][j] + res[-1][j+1])
            cur_row.append(1)
            res.append(cur_row) 
            
        return res
