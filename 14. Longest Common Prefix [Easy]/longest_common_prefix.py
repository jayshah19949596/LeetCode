class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        results, char_idx = [], 0

        while char_idx<len(strs[0]):
            # Character to compare
            char = strs[0][char_idx]
            for i in range(1, len(strs)):
                if char_idx==len(strs[i]) or strs[i][char_idx] != char:
                    return "".join(results)
            results.append(char)
            char_idx += 1

        return "".join(results)
