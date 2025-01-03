import heapq
from collections import defaultdict
from typing import List

"""
============================
## APPROACH 1: Sorting
============================
"""
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        sorted_nums_by_freq = sorted(num_freq, key=num_freq.get, reverse=True)
        return sorted_nums_by_freq[:k]

"""
============================
## APPROACH 2: Using Heap

### 1. Solution Explanation:
----------------------------
The first step is to build a hash map element -> its frequency
The second step is to build a heap of size k using N elements.
To add the first k elements takes a linear time O(k) in the average case, and O(log1+log2+...+logk)=O(logk!)=O(klogk) in the worst case

### 2. Complexity Analysis:
----------------------------
Time Complexity: O(N*LogK)
Space Complexity: O(N+K)
============================
"""
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


"""
============================
# APPROACH 3: Quickselect with Lomutos Partition
============================

### 1. Solution Explanation:
----------------------------
We can use the same algorithm to remove the invalid "(" in Approach-1.
We just need to look at the string in reverse. We do this by swapping the "(" and ")" for each other,
and reversing the order of all characters in the string
So then we can remove those characters,
and undo the reverse operation by reversing all characters and swapping "(" and ")" again,
and we have the answer

### 2. Complexity Analysis:
----------------------------
Time Complexity: O(N), in avg case. O(N^2) in worst case. Worst case probability is negligible.
Space Complexity: O(N)
"""
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def lomutos_partition(arr, low, high):
            
            part_idx = high
            part_ele = arr[part_idx][1]
            i = low
            
            for j in range(low, high):
                if arr[j][1] <= part_ele:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[part_idx] = arr[part_idx], arr[i]
            return i 

        def create_freq_arr(arr):
            freq_map = defaultdict(int)
            for num in arr:
                freq_map[num] += 1
            freq_arr = []
            for num in freq_map:
                freq_arr.append([num, freq_map[num]])
            return freq_arr

        freq_nums = create_freq_arr(nums)
        n = len(freq_nums)-1
        left, right, k = 0, n, n-k
        while left<=right:
            new_part_idx = lomutos_partition(freq_nums, left, right)
            if new_part_idx == k:
                break
            elif new_part_idx > k: right = new_part_idx - 1
            else: left = new_part_idx + 1

        return [freq_nums[i][0] for i in range(n, k, -1)]
