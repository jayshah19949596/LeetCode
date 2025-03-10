class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = defaultdict(int)
        start = longest = 0
        substr = ""
        for end, char in enumerate(s):
            if char in last_seen and start<=last_seen[char]:
                start = last_seen[char]+1
            last_seen[char] = end
            longest = max(longest, end-start+1)
        return longest
