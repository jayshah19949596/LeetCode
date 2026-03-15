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
