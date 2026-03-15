"""
We binary search the range [1, x//2] and compare mid² with x. 
If mid² is too large we move left, otherwise we move right. 
When the search finishes, right is the largest integer whose square is less than or equal to x, which is the integer square root.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1: return x
        
        left, right = 1, x//2

        while left<=right:
          
            sqrt_mid = (left+right)//2
            squared = sqrt_mid*sqrt_mid
          
            if squared == x:
                return sqrt_mid
            elif squared>x:
                right = sqrt_mid-1
            else:
                left = sqrt_mid+1
              
        return right
