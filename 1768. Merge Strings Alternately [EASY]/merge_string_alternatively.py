class Solution(object):
    def mergeAlternately(self, word1, word2):
        results = []
        n = max(len(word1), len(word2))

        for i in range(n):
            if i < len(word1): results.append(word1[i])
            if i < len(word2): results.append(word2[i])

        return "".join(results)