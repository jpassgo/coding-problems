# https://leetcode.com/problems/two-sum/?envType=list&envId=xyknlrg2
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

from typing import List

class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = {}
        for num in nums:
            complement_dict[num] = target - num

        for key in complement_dict.keys():
            if complement_dict[key] in complement_dict:
                return [nums.index(key), nums.index(complement_dict[key])]


solution = Solution()

solution.two_sum([3,2,4], 6)




