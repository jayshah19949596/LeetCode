"""
1244. Design A Leaderboard [MEDIUM]
https://leetcode.com/problems/valid-palindrome-iii

### 1. Question Explanation:
----------------------------
Design a Leaderboard class, which has 3 functions:

1. addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
2. top(K): Return the score sum of the top K players.
3. reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.

Initially, the leaderboard is empty

### 2. Solution Explanation:
----------------------------
Use SortedDict with HashMap
HashMap: Mapping from the playerId to their score
SoretedDict: is a BST with key as the score and value as the number of players that have that score
"""
from sortedcontainers import SortedDict


class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sorted_scores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:
        """
        Time: O(LogN)
        Space: O(N)
        """
        # The scores dictionary simply contains the mapping from the playerId to their score.
        # The sortedScores is a BST with key as the score and value as the number of players that have that score.
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sorted_scores[-score] = self.sorted_scores.get(-score, 0) + 1
        else:
            pre_score = self.scores[playerId]
            value = self.sorted_scores.get(-pre_score)
            if value == 1:
                del self.sorted_scores[-pre_score]
            else:
                self.sorted_scores[-pre_score] = value - 1
            new_score = pre_score + score
            self.scores[playerId] = new_score
            self.sorted_scores[-new_score] = self.sorted_scores.get(-new_score, 0) + 1

    def top(self, K: int) -> int:
        """
        Time: O(K)
        Space: O(N)
        """
        count, total = 0, 0
        for key, value in self.sorted_scores.items():
            times = self.sorted_scores.get(key)
            for _ in range(times):
                total += -key
                count += 1
                if count == K:
                    return total

    def reset(self, playerId: int) -> None:
        """
        Time: O(LogN)
        Space: O(N)
        """
        pre_score = self.scores[playerId]
        if self.sorted_scores[-pre_score] == 1:
            del self.sorted_scores[-pre_score]
        else:
            self.sorted_scores[-pre_score] -= 1
        del self.scores[playerId]
