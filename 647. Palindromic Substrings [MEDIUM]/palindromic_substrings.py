class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for center in range(2*len(s)-1):
            left = center//2 
            right = left + (center%2) # For even "center", right=left ELSE right=left+1  
            while left>=0 and right<len(s) and s[left] == s[right]:
                total += 1
                left, right = left-1, right+1
        return total
