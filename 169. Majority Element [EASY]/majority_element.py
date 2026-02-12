class Solution:
    """
    Boyer-Moore Voting Algorithm
    Idea: If we pair each occurrence of the majority element with a different element, 
    then majority element will still remain at the end because it appears > n/2 times.
    """
    def majorityElement(self, nums):
        
        count, candidate = 0, None
        for num in nums:

            # If count drops to 0, choose current number as a new candidate.
            # This means previous candidate has been "balanced out".
            if count == 0:
                candidate = num

            # If current number matches candidate, increase vote count.
            if num == candidate:
                count += 1
                # If candidate already appears more than half then return it.
                if count == len(nums) / 2:
                    return candidate
            else:
                # Otherwise, cancel out one vote.
                count -= 1

        # At the end, candidate holds the majority element
        # because majority element always survives cancellation.
        return candidate



from collections import Counter
class Solution:
    def majorityElement(self, nums):
        num_count = Counter(nums)
        for num in num_count:
            if num_count[num]>=len(nums)/2:
                return num
        
