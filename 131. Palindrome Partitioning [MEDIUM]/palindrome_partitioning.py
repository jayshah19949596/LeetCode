from collections import defaultdict

"""
APPROACH 1: BRUTE FORCE
If any prefix of s is a palindrome, then recursively partition the suffix into palindromes

Time - O(N*2^N), where N is the length of string "s"
Space - O(N)
"""
from typing import List


class Solution(object):
    def partition(self, s: str) -> List[List[str]]:
        partitons = []
        self.find_partitions(s, [], partitons)
        return partitons

    def find_partitions(self, s, partial, partitions):

        if not s:
            partitions.append(partial)
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix == prefix[::-1]:
                self.find_partitions(s[i:], partial + [s[:i]], partitions)


"""
APPROACH 1: MEMOIZATION

Time - O(N*2^N), where N is the length of string "s"
Space - O(N)
"""


class Solution:

    def partition(self, s: str) -> List[List[str]]:

        def find_partitions_by_index(partition_idx):
            if partition_idx in memo:
                return memo[partition_idx]
            output = []

            start_idx = partition_idx
            for end_idx in range(partition_idx + 1, n + 1):
                if s[start_idx: end_idx] == s[start_idx: end_idx][::-1]:
                    if end_idx == n:
                        output.append([s[start_idx: end_idx]])
                        break
                    all_partitions = find_partitions_by_index(end_idx)
                    for partition in all_partitions:
                        output.append([s[start_idx: end_idx]] + partition)
            memo[partition_idx] = output
            return output

        n = len(s)
        memo = {}
        final_output = find_partitions_by_index(0)
        return final_output
