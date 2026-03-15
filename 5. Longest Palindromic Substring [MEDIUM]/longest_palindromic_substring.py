class Solution:
    def longestPalindrome(self, s: str) -> str:
        long_r = long_l = longest = 0
        
        for center in range(2*len(s)-1):
            l = center//2
            r = l + center%2
            
            while l>=0 and r<len(s) and s[l] == s[r]:
                l, r = l-1, r+1
            else:
                l, r = l+1, r-1
            
            if longest<r-l+1:
                longest, long_r, long_l = r-l+1, r, l
                
        return s[long_l:long_r+1]
