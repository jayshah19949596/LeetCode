# Maintain 2 heaps, upperr with values >= median and lower
# with values <= median. If window is odd length, upper
# contains the odd value. Fill heaps with initial window then
# iterate over remaining nums. At star of each iteration
# balance = 0. Add median to result, add start of old window
# to junk and add end of window to new heap, both times
# updating balance. If imbalance then shift a num from
# one heap to the other. Remove junk from top of heaps.
# Time - O(n log k)
# Space - O(n)

from collections import defaultdict
import heapq

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        #max.  #min
        lower, upper = [], []           # heaps of nums in window

        for i in range(k):              # push k nums onto upper
            #  is allowed to store, at worst, one more element than the max-heap "lower"
            heapq.heappush(upper, nums[i])
        for i in range(k // 2):         # swap k//2 nums onto lower
            heapq.heappush(lower, -heapq.heappop(upper))

        medians = []
        junk = defaultdict(int)  # key is num, val is count

        for i in range(k, len(nums)):

            if k % 2 == 1:
                medians.append(float(upper[0]))
            else:
                medians.append((upper[0] - lower[0]) / 2.0)

            balance = 0     # +ve implies surplus in upper, -ve is surplus in lower

            if nums[i - k] >= upper[0]:
                balance -= 1
            else:
                balance += 1
            junk[nums[i - k]] += 1

            if nums[i] >= upper[0]:
                balance += 1
                heapq.heappush(upper, nums[i])
            else:
                balance -= 1
                heapq.heappush(lower, -nums[i])

            # balance == +2 OR -2 or 0
            # if either heap has a surplus, it's top value cannot be junk
            if balance > 0:
                heapq.heappush(lower, -heapq.heappop(upper))
            elif balance < 0:
                heapq.heappush(upper, -heapq.heappop(lower))

            while upper and upper[0] in junk:
                removed = heapq.heappop(upper)
                junk[removed] -= 1
                if junk[removed] == 0:
                    del junk[removed]
            while lower and -lower[0] in junk:
                removed = -heapq.heappop(lower)
                junk[removed] -= 1
                if junk[removed] == 0:
                    del junk[removed]

        if k % 2 == 1:
            medians.append(float(upper[0]))
        else:
            medians.append((upper[0] - lower[0]) / 2.0)
        return medians