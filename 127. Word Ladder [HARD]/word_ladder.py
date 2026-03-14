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


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord) != len(endWord): return 0
        word_set = set(wordList)
        for word in wordList:
            if len(word) == len(beginWord):
                word_set.add(word)
        if len(word_set) == 0: return 0
        if endWord not in word_set: return 0

        queue = deque([[beginWord, 1]])
        visited = set([beginWord])
        while queue:
            cur_word, cur_dist = queue.pop()
            if cur_word == endWord: return cur_dist
            for nxt_word in word_set:
                diff = 0
                for i in range(len(cur_word)):
                    if cur_word[i] != nxt_word[i]: diff += 1
                if diff == 1 and nxt_word not in visited:
                    visited.add(nxt_word)
                    queue.appendleft([nxt_word, cur_dist+1])
        return 0
