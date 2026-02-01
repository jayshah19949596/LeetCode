from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = max_freq = result = 0

        for right in range(len(s)):
            count[s[right]] = count[s[right]]+1
            max_freq = max(max_freq, count[s[right]])

            # If replacements needed > k, shrink window
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
