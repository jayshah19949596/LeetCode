
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []      # holds (prev_str, repeat_count)
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)

            elif char == "[":
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0

            elif char == "]":
                prev_str, prev_num = stack.pop()
                curr_str = prev_str + curr_str * prev_num

            else:
                curr_str += char

        return curr_str



class Solution:
    def decodeString(self, encoded_string):
        """
        :type encoded_string: str
        :rtype: str
        """
        stack = [["", 1]]          # [current_substring, repeat_count]
        index = 0
        repeat_digits = ""

        for index in range(len(encoded_string)):
            char = encoded_string[index]

            if char.isdigit():
                repeat_digits += char

            elif char == "[":
                stack.append(["", int(repeat_digits)])
                repeat_digits = ""

            elif char == "]":
                decoded_part, repeat_count = stack.pop()
                stack[-1][0] += decoded_part * repeat_count

            else:
                stack[-1][0] += char


        return stack[0][0]
