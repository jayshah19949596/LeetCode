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
Use HashMap to maintain the player to score mapping.
Use Heap data structure to get to K player and sum their score.
"""
from collections import defaultdict
from heapq import heappush, heappop


class Leaderboard:
    def __init__(self):
        self.scoreboard = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        """
        Time Complexity: O(1)
        Space Complexity: O(N), N is number of player played so far in "self.scoreboard"
        """
        self.scoreboard[playerId] += score

    def top(self, K: int) -> int:
        """
        Time Complexity: O(N*LogK)
        Space Complexity: O(N+K)
            Where N = len(self.scoreboard)
            And K = len(heap)
        """
        heap_arr = []
        for playerId in self.scoreboard:
            heappush(heap_arr, self.scoreboard[playerId])
            if len(heap_arr) > K: heappop(heap_arr)
        return sum(heap_arr)

    def reset(self, playerId: int) -> None:
        """
        Time Complexity: O(1)
        Space Complexity: O(N), N is number of player played so far in "self.scoreboard"
        """
        del self.scoreboard[playerId]
