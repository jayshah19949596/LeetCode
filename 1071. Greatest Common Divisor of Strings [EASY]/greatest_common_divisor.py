"""
Ref: https://leetcode.com/problems/greatest-common-divisor-of-strings/editorial/
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        def valid(base_length):
            if len1 % k !=0 or len2 % k != 0:  return False
                
            n1, n2 = len1 // base_length, len2 // base_length
            base = str1[:base_length]
            return str1 == n1 * base and str2 == n2 * base 
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""


import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = math.gcd(len(str1), len(str2))
        return str1[:max_length]
