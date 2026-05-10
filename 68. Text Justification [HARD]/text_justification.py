# https://leetcode.com/problems/text-justification/
# Given an array of words and a length L, format the text such that each
# line has exactly L characters and is fully (left and right) justified.
# Pack as many words as you can in each line. Pad extra spaces
# ' ' when necessary so that each line has exactly L characters.
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words, the empty
# slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left justified
# and no extra space is inserted between words.
# Each word is guaranteed not to exceed L in length.

# Fill lines with words and single spaces until full.
#  Then justify by distributing remaining spaces
# Time - O(maxWidth * nb_lines)
# Space - O(maxWidth * nb_lines)

class Solution(object):
    def fullJustify(self, words, maxWidth):
        line_chars = 0          # number of chars on current line (without spaces)
        line_words = []         # list of words on current line
        justified = []          # output, list of justified strings

        for word in words:
            # Check if adding this word (plus at least one space per existing word) exceeds maxWidth
            if line_chars + len(line_words) + len(word) > maxWidth:
                gaps = len(line_words) - 1
                spaces = maxWidth - line_chars
                
                if gaps == 0:
                    # Case: Only one word on the line
                    line_str = line_words[0] + (" " * spaces)
                else:
                    # Case: Multiple words, distribute spaces evenly
                    line = [line_words[0]]
                    for i in range(1, len(line_words)):
                        # Distribute spaces: current_spaces // remaining_gaps (rounded up if needed)
                        space_count = spaces // gaps
                        if spaces % gaps != 0:          # round up if uneven division of spaces
                            space_count += 1 
                        line.append(" " * space_count)
                        line.append(line_words[i])
                        spaces -= space_count
                        gaps -= 1
                    line_str = "".join(line)
                
                justified.append(line_str)
                # Reset for the next line
                line_words = []
                line_chars = 0

            # Always add the current word to the (potentially new) line
            line_words.append(word)
            line_chars += len(word)

        # Handle the last line: Left justified
        final_line = " ".join(line_words)
        # Pad the remainder of the last line with spaces
        final_line += " " * (maxWidth - len(final_line))
        justified.append(final_line)

        return justified
