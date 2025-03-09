"""
----------------------
Approach 1: Simulation: Write as you go
----------------------
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = anchor_idx = 0
        while i<len(chars):
            cur_char = chars[i]
            count = 0
            while i<len(chars) and cur_char == chars[i]:
                i += 1
                count += 1
            else: i -= 1

            chars[anchor_idx] = cur_char
            anchor_idx += 1
            if count>1:
                count_str = str(count)
                for count_char in count_str:
                    chars[anchor_idx] = count_char
                    anchor_idx += 1
            i += 1
        return anchor_id


"""
----------------------
Approach 2: Simulation: Write at terminating condition when chars are not equal 
----------------------
"""
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write
