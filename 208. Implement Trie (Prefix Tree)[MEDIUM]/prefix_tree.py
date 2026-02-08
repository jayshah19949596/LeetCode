class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.is_end = False
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.is_end] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.trie
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.is_end in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.trie
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
