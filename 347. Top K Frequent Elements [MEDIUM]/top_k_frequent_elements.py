import heapq
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = defaultdict(int)
        for num in nums: frequency_map[num] += 1

        heap_results = []
        for num in frequency_map:
            heapq.heappush(heap_results, (frequency_map[num], num))
            if len(heap_results) > k:
                heapq.heappop(heap_results)

        return [result[1] for result in heap_results]