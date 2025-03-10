class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest  = ""
        
        for center in range(2*len(s)-1):
            left = center//2
            right = left+(center%2)
            
            while left>= 0 and right<len(s) and s[left] == s[right]:
                left, right = left-1, right+1
            else:
                left, right = left+1, right-1
            
            if right-left+1 > len(longest):
                longest = s[left:right+1]
            
        return longest
