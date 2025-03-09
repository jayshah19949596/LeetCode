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
