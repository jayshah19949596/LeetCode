"""
Reference: https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/solutions/6105416/well-explained-beginner-friendly-solution-o-n-solution-beats-100-solutions/

====================================
Intuition
====================================
To solve this problem, we need to find the largest potential outlier in an array where:

( n - 2 ) elements are special numbers.
One element is the sum of the special numbers.
One element is the outlier, which is distinct from both the sum element and the special numbers.
The problem hints that we can leverage the relationship between the sum of all elements and the sum of special numbers. Specifically, the sum of all elements in the array is related to the sum of the special numbers, their sum, and the outlier. This relationship can be described by the equation:

total_sum=2×(sum of special numbers)+(outlier)

The task is to find the largest outlier, given that there is one candidate that is the sum of the special numbers and the rest are special numbers.
====================================
Approach
====================================
To solve this efficiently, I’ll break down the approach as follows:

Calculate the Total Sum of All Elements:
First, compute the sum of all elements in the array (total_sum). This will help us later in identifying potential outliers.

Count Frequencies of Elements:
Use a dictionary (num_counts) to track the frequency of each number in the array. This helps in quickly checking whether a number exists in the array when needed.

Identify Possible Outliers:
For each unique number num in the array, treat it as a candidate for the sum of the special numbers. The potential outlier is calculated using the formula:
potential_outlier=total_sum−2×num
This formula comes from the equation:
outlier=total_sum−2×sum of special numbers

Check Validity of Potential Outlier:
For each candidate number, check if the calculated potential outlier exists in the array. Ensure that the outlier is distinct from the candidate number, unless the candidate appears multiple times in the array.

Track the Largest Outlier:
Throughout the iteration, keep track of the largest valid outlier and return that as the result.


"""
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = 0
        num_counts = defaultdict(int)
        for num in nums:
            total_sum += num
            num_counts[num] += 1

        largest_outlier = float('-inf')
        for num in num_counts.keys():
            potential_outlier = total_sum - 2 * num
            if ( potential_outlier in num_counts and 
                 (potential_outlier != num or num_counts[num] > 1)
               ): 
                largest_outlier = max(largest_outlier, potential_outlier)
        return largest_outlier
