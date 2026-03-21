"""
BINARY ADDITION RULES (A + B + Carry):
--------------------------------------
Sum = 0  ->  Write 0, Carry 0
Sum = 1  ->  Write 1, Carry 0
Sum = 2  ->  Write 0, Carry 1  (This covers 1+1+0 and 1+0+1)
Sum = 3  ->  Write 1, Carry 1  (This is 1+1+1)

"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            # Get values or 0 if pointer is exhausted
            v1 = 0
            if i >= 0:
                v1 = ord(a[i]) - ord('0')
            v2 = 0
            if j >= 0:
                v2 = ord(b[j]) - ord('0') 
            
            # Calculate sum of current column
            current_sum = v1 + v2 + carry
            
            # Binary math: Bit = sum mod 2
            # Carry = sum floor-div 2
            res.append(str(current_sum % 2))
            carry = current_sum // 2
            
            i -= 1
            j -= 1
            
        return "".join(res[::-1])
