class Trie:
    def __init__(self):
        self.trie = defaultdict(str)

    # Insert a number into the Trie by treating it as a string of digits
    def insert(self, num):
        node = self.trie
        for digit in str(num):
            if digit not in node:
                node[digit] = defaultdict(str)
            node = node[digit]

    # Find the longest common prefix for a number in arr2 with the Trie
    def find_longest_prefix(self, num):
        node, length = self.trie, 0
        for digit in str(num):
            if digit not in node: break 
            node = node[digit]
            length += 1
        return length


class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        trie = Trie()

        # Step 1: Insert all numbers from arr1 into the Trie
        for num in arr1:
            trie.insert(num)

        max_longest_prefix = 0

        # Step 2: Find the longest prefix match for each number in arr2
        for num in arr2:
            cur_longest_length = trie.find_longest_prefix(num)
            max_longest_prefix = max(max_longest_prefix, cur_longest_length)

        return max_longest_prefix
