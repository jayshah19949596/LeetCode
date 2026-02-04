class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start = longest = 0
        for end, char in enumerate(s):
            """
            2nd condition is to only move "start" if the repeated char is with-in current window else wihtout it start can go backwards.
            Failure case : s = "abba"
            """
            if char in last_seen and start<=last_seen[char]: 
                start = last_seen[char]+1
            last_seen[char] = end
            longest = max(longest, end-start+1)
        return longest
