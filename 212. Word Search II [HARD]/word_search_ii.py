from typing import List


class Trie:
    def __init__(self):
        self.trie = {}

    def create_trie(self, word):
        node = self.trie
        for char in word:
            if char in node:
                node = node[char]
            else:
                node[char] = {}
                node = node[char]
        else:
            node['end'] = None

    def find_prefix(self, prefix):
        prev_node = None
        node = self.trie

        for char in prefix:
            if char not in node:
                return False, False
            else:
                prev_node = node
                node = node[char]

        is_end = 'end' in node
        if is_end or len(node) == 0 and prev_node is not None:
            prev_node = {}
        return True, is_end


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        neighbor_row, neighbor_col = [0, 1, 0, -1], [1, 0, -1, 0]

        def recurse_dfs(board, prefix, cell_path, visited, cur_cell):
            cur_row, cur_col = cur_cell
            is_prefix, is_full_word = trie.find_prefix(prefix)

            if not is_prefix:
                return

            if is_full_word:
                results.add(prefix)

            for nr, nc in zip(neighbor_row, neighbor_col):
                new_r, new_c = cur_row + nr, cur_col + nc
                if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]) and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    recurse_dfs(board, prefix + board[new_r][new_c], cell_path + [(new_r, new_c)], visited,
                                (new_r, new_c))
                    visited.remove((new_r, new_c))

        trie = Trie()
        max_len = 0
        for word in words:
            max_len = max(max_len, len(word))
            trie.create_trie(word)

        results = set([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                recurse_dfs(board, board[r][c], [(r, c)], set([(r, c)]), (r, c))
        return list(results)

