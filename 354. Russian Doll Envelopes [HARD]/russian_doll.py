class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # Step 1: Sort strategy.
        # Sort by width ascending. For identical widths, sort height DESCENDING.
        # This prevents us from counting two envelopes with the same width 
        # (e.g., [3,4] and [3,5]) as nestable, because 5 is not > 5 in height.
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Step 2: LongestIncreasingSubseq(LIS) on heights.
        # 'tails' stores the smallest possible tail (height) for all increasing 
        # subsequences of length 'i + 1'.
        tails = []

        for _, height in envelopes:
            # We want to find where this 'height' fits in our existing nesting chain.
            # We use binary search to find the insertion point in O(log N).
            insertion_idx = self.find_insertion_point(tails, height)

            if insertion_idx == len(tails):
                # If the current height is greater than all existing tails,
                # we have found a way to create a longer Russian Doll chain.
                tails.append(height)
            else:
                # Otherwise, replace the existing tail at this index with the 
                # smaller height. This "greedily" keeps our height low to 
                # allow more envelopes to fit in the future.
                tails[insertion_idx] = height

        return len(tails)

    def find_insertion_point(self, tails, target_height):
        """
        Standard Binary Search (bisect_left) to find the index of the 
        first element in 'tails' that is >= target_height.
        """
        low, high = 0, len(tails) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if tails[mid] < target_height:
                # Target is taller, look to the right
                low = mid + 1
            else:
                # Current tail is already taller or equal, look to the left
                high = mid - 1
                
        return low
