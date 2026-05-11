class Solution:
    def reverse(self, num: int) -> int:
        negative = False
        if num < 0:
            num = abs(num)
            negative = True
        
        reverse_num = 0
        while num != 0:
            remainder = num % 10
            reverse_num = reverse_num * 10 + remainder
            num = num // 10
            if reverse_num > 2**31-1: return 0
        
        if negative:
            return -reverse_num
        return reverse_num
