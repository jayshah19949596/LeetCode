class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord): return 0
        wordSet = set([])
        for word in wordList:
            if len(word) == len(beginWord):
                wordSet.add(word)
        if len(wordSet) == 0: return 0

        if endWord not in wordSet:
            return 0  # If endWord isn't in the wordList, no possible transformation
        
        queue = deque([(beginWord, 1)])  # (current word, transformation steps)
        
        while queue:
            word, steps = queue.popleft()
            
            if word == endWord:
                return steps  # Found the shortest transformation
            
            # Try changing each character in the word
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + char + word[i+1:]
                    if newWord in wordSet:
                        queue.append((newWord, steps + 1))
                        wordSet.remove(newWord)  # Remove from wordSet to prevent revisits

        return 0  # No transformation sequence found
