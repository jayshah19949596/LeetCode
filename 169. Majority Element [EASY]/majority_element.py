class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate: 
              count += 1
              if count == len(nums)/2: return candidate
            else: count -=1
        return candidate


from collections import Counter
class Solution:
    def majorityElement(self, nums):
        num_count = Counter(nums)
        for num in num_count:
            if num_count[num]>=len(nums)/2:
                return num
        
