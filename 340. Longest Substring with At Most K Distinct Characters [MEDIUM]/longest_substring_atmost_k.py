class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        start = longest = 0
        last_seen = {}

        for end, char in enumerate(s):
            last_seen[char] = end
            while len(last_seen) > k:
                last_seen[s[start]] -= 1
                if last_seen[s[start]] == 0: 
                    del last_seen[s[start]]
                start += 1

            longest = max(longest, end-start+1)
        return longest
