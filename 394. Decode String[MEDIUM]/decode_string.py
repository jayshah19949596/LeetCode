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
