"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

### 1. Question Explanation:
----------------------------
Given two sparse vectors, compute their dot product.
Implement class SparseVector:
SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.
Follow up: What if only one of the vectors is sparse?

#### Example 1:
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

#### Example 2:
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

#### Example 3:
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
"""
from typing import List
from collections import defaultdict


# APPROACH 1: Non-efficient Array Approach
class SparseVector:
    """
    Ignore the sparsity of the array and store the original array.

    Complexity Analysis:
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def __init__(self, nums: List[int]):
        self.array = nums

    def dotProduct(self, vec):
        result = 0
        for num1, num2 in zip(self.array, vec.array):
            result += num1 * num2
        return result

# APPROACH 2: Hash Map
class SparseVector:
    """
    Store the non-zero values and their corresponding indices in a dictionary, with the index being the key. Any index that is not present corresponds to a value 0 in the input array.

    Complexity Analysis:
    Time Complexity: O(N) for creating the Hash Map; O(L) for calculating the dot product.
    Space Complexity: O(L) for creating the Hash Map
    """

    def __init__(self, nums: List[int]):
        self.idx_to_value = defaultdict(int)
        for i, num in enumerate(nums):
            if num != 0: self.idx_to_value[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        answer, i = 0, 0
        for key in self.idx_to_value:
            if i >= len(vec.idx_to_value): break
            answer += vec.idx_to_value[key] * self.idx_to_value[key]
            i += 1
        return answer


# APPROACH 2: Index-Value Pairs with TWO Pointer approach for dot-product
class SparseVector:
    """
    represent elements of a sparse vector as a list of <index, value> pairs.
    Use two pointers to iterate through the two vectors to calculate the dot product.

    Complexity Analysis:
    Time Complexity: O(N) for creating the <index, value> pair for non-zero values; O(L+L2) for calculating the dot product.
    Space Complexity: O(L) for creating the <index, value> pairs for non-zero values. O(1) for calculating the dot product.
    """
    def __init__(self, nums: List[int]):
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return result