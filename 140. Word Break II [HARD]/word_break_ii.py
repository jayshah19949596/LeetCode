class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = defaultdict(list)

        # break the input string into lists of words list
        self.recurse_topdown(s, wordDict, memo)
        print(memo)
        # chain up the lists of words into sentences.
        return [" ".join(words) for words in memo[s]]

    # @lru_cache(maxsize=None)    # alternative memoization solution
    def recurse_topdown(self, s, wordDict, memo):
        """ return list of word lists """
        if len(s) == 0:
            return [[]]  # list of empty list

        if s in memo:
            # returned the cached solution directly.
            return memo[s]

        for word in wordDict:
            if s.startswith(word):
                sub_sentences = self.recurse_topdown(s[len(word):], wordDict, memo)
                for subsentence in sub_sentences:
                    memo[s].append([word] + subsentence)
                print(s, memo[s])

        return memo[s]